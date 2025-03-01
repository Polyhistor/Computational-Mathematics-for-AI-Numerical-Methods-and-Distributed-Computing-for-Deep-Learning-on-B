import numpy as np
import krippendorff

# Before Delphi
# data = np.array([
#     [0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,0,0,0],
#     [1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,1],
#     [1,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,0,0],
#     [0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
#     [1,1,0,0,1,0,0,0,1,1,0,1,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,0,0]
# ])

# Data from the CSV (5 raters, 28 papers) - Delphi 2
data = np.array([
    [0,1,0,0,1,0,1,1,1,0,0,0,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1],
    [1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0],
    [1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0],
    [1,1,1,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,0,1,0],
    [0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,1,0,1,0]
])

def analyze_agreement(data):
    # Calculate Krippendorff's alpha
    alpha = krippendorff.alpha(reliability_data=data, level_of_measurement='nominal')
    
    # Calculate agreement statistics
    n_papers = data.shape[1]
    n_raters = data.shape[0]
    
    # Calculate agreement per paper
    agreements = []
    for paper_idx in range(n_papers):
        votes = data[:, paper_idx]
        yes_count = np.sum(votes == 1)
        no_count = np.sum(votes == 0)
        agreement_rate = max(yes_count, no_count) / n_raters * 100
        agreements.append({
            'paper_idx': paper_idx + 1,
            'agreement_rate': agreement_rate,
            'yes_count': yes_count,
            'no_count': no_count
        })
    
    # Sort papers by agreement rate
    agreements.sort(key=lambda x: x['agreement_rate'])
    
    return alpha, agreements

def print_analysis(alpha, agreements):
    print(f"Krippendorff's alpha: {alpha:.4f}")
    print("\nInterpretation:")
    if alpha >= 0.8:
        print("Strong agreement (α ≥ 0.8)")
    elif alpha >= 0.667:
        print("Tentative agreement (0.667 ≤ α < 0.8)")
    else:
        print("Low agreement (α < 0.667)")
    
    print("\nOverall Statistics:")
    avg_agreement = np.mean([a['agreement_rate'] for a in agreements])
    print(f"Average agreement rate: {avg_agreement:.2f}%")
    
    print("\nPapers with lowest agreement (most disagreement):")
    for paper in agreements[:5]:
        print(f"\nPaper {paper['paper_idx']}:")
        print(f"Agreement rate: {paper['agreement_rate']:.2f}%")
        print(f"Yes votes: {paper['yes_count']}, No votes: {paper['no_count']}")

# Run the analysis
alpha, agreements = analyze_agreement(data)
print_analysis(alpha, agreements)