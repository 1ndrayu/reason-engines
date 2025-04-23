import json

# Helper function to read JSON file
def read_input_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "File not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}

# Component 1: Confidence-Scoring Algorithm for Source Reliability
def confidence_score_source(file_path):
    """
    Assigns a confidence score to a data source from a JSON file.
    Input: File path to JSON with source metadata.
    Output: Confidence score (0-1) or error message.
    """
    data = read_input_file(file_path)
    if "error" in data:
        return data["error"]
    
    source_data = data.get("confidence_score", {}).get("source", {})
    if not source_data:
        return "No source data provided"
    
    weights = {
        'source_type': 0.4,  # Primary (0.9), secondary (0.6), opinion (0.3)
        'recency': 0.3,      # Years since publication
        'authority': 0.3     # Credibility of publisher
    }
    
    score = 0.0
    
    # Source type score
    source_types = {'primary': 0.9, 'secondary': 0.6, 'opinion': 0.3}
    score += weights['source_type'] * source_types.get(source_data.get('type', 'opinion'), 0.3)
    
    # Recency score (linear decay, max 5 years)
    years_old = 2025 - source_data.get('year', 2025)
    recency_score = max(0, 1 - (years_old / 5))
    score += weights['recency'] * recency_score
    
    # Authority score
    authorities = {'academic': 0.9, 'government': 0.8, 'news': 0.5, 'blog': 0.2}
    score += weights['authority'] * authorities.get(source_data.get('authority', 'blog'), 0.2)
    
    return min(max(score, 0.0), 1.0)

# Component 2: Decision-Rule Engine for Problem Complexity
def decision_rule_engine(file_path):
    """
    Determines analysis depth from query metadata in a JSON file.
    Input: File path to JSON with query features.
    Output: Analysis mode ('light', 'moderate', 'deep') or error message.
    """
    data = read_input_file(file_path)
    if "error" in data:
        return data["error"]
    
    query_metadata = data.get("decision_rule", {}).get("query", {})
    if not query_metadata:
        return "No query data provided"
    
    complexity_score = 0
    
    # Keyword complexity
    keywords = query_metadata.get('keywords', [])
    technical_terms = ['quantum', 'tariff', 'algorithm', 'philosophy']
    complexity_score += sum(1 for kw in keywords if kw.lower() in technical_terms)
    
    # Domain complexity
    domains = {'science': 2, 'economics': 2, 'history': 1, 'general': 0}
    complexity_score += domains.get(query_metadata.get('domain', 'general'), 0)
    
    # Urgency penalty
    urgency = query_metadata.get('urgency', 'normal')
    urgency_modifier = {'high': -1, 'normal': 0, 'low': 1}
    complexity_score += urgency_modifier.get(urgency, 0)
    
    # Decision rules
    if complexity_score <= 1:
        return 'light'
    elif complexity_score <= 3:
        return 'moderate'
    else:
        return 'deep'

# Component 3: Consensus-Evaluation Module
def evaluate_consensus(file_path):
    """
    Evaluates if a claim aligns with high-evidence consensus from a JSON file.
    Input: File path to JSON with claim and sources.
    Output: Consensus status ('supported', 'disputed', 'no_consensus') or error message.
    """
    data = read_input_file(file_path)
    if "error" in data:
        return data["error"]
    
    consensus_data = data.get("consensus_eval", {})
    claim = consensus_data.get("claim", "")
    sources = consensus_data.get("sources", [])
    
    if not claim or not sources:
        return "No claim or sources provided"
    
    # Calculate confidence scores for sources
    high_conf_sources = []
    for source in sources:
        temp_source = source.copy()
        score = confidence_score_source({"confidence_score": {"source": temp_source}})
        if isinstance(score, float) and score >= 0.7:
            high_conf_sources.append(source)
    
    if not high_conf_sources:
        return 'no_consensus'
    
    # Count support/opposition (simplified: keyword match)
    support_count = 0
    oppose_count = 0
    for source in high_conf_sources:
        content = source.get('content', '').lower()
        if claim.lower() in content:
            support_count += 1
        elif f"not {claim.lower()}" in content:
            oppose_count += 1
    
    total = support_count + oppose_count
    if total == 0:
        return 'no_consensus'
    support_ratio = support_count / total
    if support_ratio >= 0.8:
        return 'supported'
    elif support_ratio <= 0.2:
        return 'disputed'
    else:
        return 'no_consensus'

# Component 4: Hybrid Reasoning Engine
def hybrid_reasoning_engine(file_path):
    """
    Combines deductive and inductive reasoning using data from a JSON file.
    Input: File path to JSON with problem and data points.
    Output: Conclusion string or error message.
    """
    data = read_input_file(file_path)
    if "error" in data:
        return data["error"]
    
    reasoning_data = data.get("hybrid_reasoning", {})
    problem = reasoning_data.get("problem", "")
    data_points = reasoning_data.get("data", [])
    
    if not problem:
        return "No problem provided"
    
    # Deductive: Start with first principles
    first_principles = {
        'economics': 'Supply and demand govern prices.',
        'physics': 'Energy is conserved.'
    }
    domain = data_points[0].get('domain', 'general') if data_points else 'general'
    base_principle = first_principles.get(domain, 'General reasoning applies.')
    
    # Inductive: Generalize from data
    observations = [d.get('observation', '') for d in data_points]
    if not observations:
        return f"Based on {base_principle}, insufficient data to conclude."
    
    # Simple pattern detection
    positive_outcomes = sum(1 for obs in observations if 'increase' in obs.lower())
    total = len(observations)
    trend = 'likely increases' if positive_outcomes / total > 0.5 else 'may not increase'
    
    # Combine deductive and inductive
    if domain == 'economics' and 'price' in problem.lower():
        conclusion = f"{base_principle} Data suggests {problem.lower()} {trend}."
    else:
        conclusion = f"{base_principle} Data analysis inconclusive for {problem}."
    
    return conclusion

# Example usage: Run all components with a single JSON file
def run_framework(file_path):
    print("Confidence Score:", confidence_score_source(file_path))
    print("Analysis Mode:", decision_rule_engine(file_path))
    print("Consensus Status:", evaluate_consensus(file_path))
    print("Conclusion:", hybrid_reasoning_engine(file_path))

# Call with your JSON file path
if __name__ == "__main__":
    file_path = "input.json"  # Replace with your file path
    run_framework(file_path)
