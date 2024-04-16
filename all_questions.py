import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.008  
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = '0.5 * math.log((1 - p) / p)'

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.527
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = 'No'

    # type: explain_string
    answers['Explain'] = "In Alan's scenario, employing a coin flip as a model is overly simplistic and lacks relevance to the intricate dynamics of the stock market. Each coin toss operates in isolation, devoid of any connection or learning from prior events. Consequently, the collective outcome of multiple coin flips fails to offer any meaningful indication of whether the stock market will experience an upturn or downturn"

    
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = 'Both classifiers, C1 and C2, exhibit identical performance as they both lie along the random guess line on the ROC curve.'

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) explain'] = " While precision and recall favor Classifier C2 for its higher recall rate, they fail to account for false positives. True positive rate (TPR) and false positive rate (FPR) provide a more nuanced assessment, acknowledging Classifier C2's elevated recall alongside its increased likelihood of false positives. This makes TPR and FPR better suited for evaluating relative performance, particularly in contexts where false positives hold significant implications."
    
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = 'C2 accurately identifies a greater portion of true positive cases while maintaining a superior equilibrium between precision and recall.'

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = 'Precision, recall, and F1-measure offer a more comprehensive evaluation of classifiers C1 and C2, taking into account their effectiveness in correctly detecting positive instances and their capability to mitigate false positives, in contrast to solely considering TPR and FPR.'

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C3'

    # type: explain_string
    answers['(iii) best classifier, explain'] = "C3 surpasses C1 in both precision and recall while upholding an equal false positive rate (FPR). Although it doesn't match C2 in recall and F1-measure, C3 presents a superior overall balance compared to C1 and C2, making it the preferred option among the three."
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] =  "1/10"

    # type: eval_float
    answers['(a) recall for C0'] =  "p"

    # type: eval_float
    answers['(b) F-measure of C0'] = "(0.2*p)/(0.1+p)"

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'no'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {
    'recall': 0.533,
    'precision': 0.615,
    'F-measure': 0.571,
    'accuracy': 0.88
}

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = 'The F-measure, unlike accuracy, takes into account class imbalance, offering a more balanced evaluation by considering both precision and recall.'
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'F1'

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = 'Given the stakes involved in cancer detection, where false positives can trigger unwarranted medical procedures and patient distress, and false negatives can mean missed chances for treatment, it is imperative to prioritize minimizing both types of errors. Hence, in this scenario, the F1-Score emerges as a more suitable evaluation metric for comparing the two tests.'

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = 'In situations where early detection is critical, such as in cancer screening, prioritizing sensitivity over specificity is vital due to the higher risks associated with false negatives compared to false positives. Consequently, metrics like the true positive rate (TPR) to false positive rate (FPR) ratio are often favored over the F1-Score, particularly when minimizing the likelihood of missed diagnoses is of utmost importance.'
    
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
