from flask import Flask, render_template, request, jsonify, session
from sentiment_analyzer import SentimentAnalyzer
from utils import TextUtils
import json

app = Flask(__name__)
app.secret_key = 'sentiment-analysis-secret-key-2024'

# Initialize analyzer
analyzer = SentimentAnalyzer()

@app.route('/')
def index():
    """Render the main page"""
    # Get sample texts for demonstration
    sample_texts = TextUtils.get_sample_texts()
    return render_template('index.html', sample_texts=sample_texts)

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    """Analyze sentiment from text input"""
    try:
        # Get text from form
        text = request.form.get('text', '').strip()
        
        if not text:
            return jsonify({
                'success': False,
                'error': 'Please enter some text to analyze.'
            })
        
        # Analyze sentiment
        result = analyzer.analyze_sentiment(text)
        
        # Extract source information
        sources = TextUtils.extract_source_info(text)
        
        # Add source information to result
        result['sources'] = sources
        
        # Store result in session for results page
        session['last_result'] = result
        
        return jsonify({
            'success': True,
            'result': result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        })

@app.route('/analyze-batch', methods=['POST'])
def analyze_batch():
    """Analyze multiple texts at once"""
    try:
        # Get texts from form
        texts_text = request.form.get('batch_text', '')
        texts = [text.strip() for text in texts_text.split('\n') if text.strip()]
        
        if not texts:
            return jsonify({
                'success': False,
                'error': 'Please enter some texts to analyze.'
            })
        
        # Limit to 50 texts to prevent overload
        if len(texts) > 50:
            texts = texts[:50]
        
        # Analyze each text
        results = []
        for text in texts:
            result = analyzer.analyze_sentiment(text)
            results.append(result)
        
        # Calculate overall statistics
        sentiment_counts = {
            'Positive': 0,
            'Negative': 0,
            'Neutral': 0
        }
        
        for result in results:
            sentiment_counts[result['sentiment']] += 1
        
        total = len(results)
        percentages = {
            sentiment: round((count / total) * 100, 2)
            for sentiment, count in sentiment_counts.items()
        }
        
        # Determine overall sentiment
        overall_sentiment = max(sentiment_counts.items(), key=lambda x: x[1])[0]
        
        batch_result = {
            'total_texts': total,
            'sentiment_counts': sentiment_counts,
            'percentages': percentages,
            'overall_sentiment': overall_sentiment,
            'results': results
        }
        
        # Store in session
        session['batch_result'] = batch_result
        
        return jsonify({
            'success': True,
            'batch_result': batch_result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        })

@app.route('/results')
def show_results():
    """Display detailed results page"""
    result = session.get('last_result', None)
    if not result:
        return render_template('index.html')
    
    return render_template('results.html', result=result)

@app.route('/batch-results')
def show_batch_results():
    """Display batch analysis results"""
    batch_result = session.get('batch_result', None)
    if not batch_result:
        return render_template('index.html')
    
    return render_template('batch_results.html', batch_result=batch_result)

@app.route('/get-sample/<int:index>')
def get_sample_text(index):
    """Get sample text by index"""
    sample_texts = TextUtils.get_sample_texts()
    if 0 <= index < len(sample_texts):
        return jsonify({
            'success': True,
            'text': sample_texts[index]
        })
    return jsonify({
        'success': False,
        'error': 'Invalid sample index'
    })

@app.route('/clear')
def clear_session():
    """Clear session data"""
    session.clear()
    return jsonify({'success': True})

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Sentiment Analysis API',
        'version': '1.0.0'
    })

if __name__ == '__main__':
    print("=" * 60)
    print("SENTIMENT ANALYSIS WEB APPLICATION")
    print("=" * 60)
    print("\nStarting server...")
    print("Initializing sentiment analyzer...")
    print("Downloading NLTK data (if required)...")
    print("\n✅ Application is ready!")
    print("\n🌐 Open your browser and visit:")
    print("   http://localhost:5000")
    print("\n📝 Enter text from:")
    print("   • Social Media (Twitter, Facebook)")
    print("   • E-commerce reviews (Amazon, Flipkart)")
    print("   • News articles")
    print("   • Customer feedback")
    print("\n🔍 Click 'Analyze Sentiment' to see results!")
    print("=" * 60)
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
