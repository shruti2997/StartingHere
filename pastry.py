# Bayesian Probability: "Nikhil eats pastry only when I clear my exam"

def nikhil_pastry_bayes():
    print("Bayesian Probability: Exam & Pastry Situation ")

    P_E = float(input("chance I clear the exam: "))
    P_P_given_E = float(input("nikhil eats pastry given I cleared: "))
    P_P_given_notE = float(input("he eats pastry given I did NOT clear: "))

    # Also,Complementary
    P_notE = 1 - P_E

    # probability of Nikhil eating pastry 
    P_P = (P_P_given_E * P_E) + (P_P_given_notE * P_notE)

    # therefore Bayes' Rule
    P_E_given_P = (P_P_given_E * P_E) / P_P


    print("\n Results:")
    print(f"Total probability Nikhil eats pastry (P(P)): {P_P:.2f}")
    print(f"Probability I cleared the exam given he ate pastry (P(E|P)): {P_E_given_P:.2f}")

    # varying conditions
    if P_E_given_P > 0.7:
        print("\n high chance I cleared the exam. Nikhil go eat pastry")
    elif P_E_given_P > 0.5:
        print("\n Fair chance I passed — no guarantee.")
    else:
        print("\n Probably not — Nikhil ate pastry secretly")

# Run the function
nikhil_pastry_bayes()
