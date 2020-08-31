dictf={
    "good":"bad",
    "Above": "below",
    "absent" :"present",
    "abundant": "scarce",
    "accept" : "decline",
    "accomplishment":"failure",
    "accurate": "inaccurate",
    "achieve":"fail",
    "add":"subtract",
    "adjacent":"distant",
    "admire" :"detest",
    "admit": "deny",
    "adore":"hate",
    "advance":"retreat",
}

def antonym(word,dictf):
    if word in dictf:
        print("Antonym of {} is {}.".format(word,dictf[word]))
    else:
        print("Not present in my dictionary of antonyms.")

w=input("Enter word to known its antonym from('good','Above','absent','abundant','accept','accomplishment','accurate','achieve','add','adjacent','admire','admit','adore','advance'): ")
word=w.lower()          
antonym(word,dictf)
