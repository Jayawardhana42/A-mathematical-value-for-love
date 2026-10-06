import time

def analyze_relationship():
    print("=" * 60)
    print("          THE REALITY CHECK: RELATIONSHIP INSIGHTS")
    print("=" * 60)
    print("Take a moment, think honestly about how she treats you,")
    print("and answer the following 10 questions.")
    print("Type 'y' for Yes or 'n' for No.\n")
    
    time.sleep(1)

    questions = [
        "1. Does she genuinely stand by your side during your absolute lowest moments?",
        "2. Can you both talk openly and honestly without fear of major secrets or lies?",
        "3. Does she truly support your real-life goals, hustle, and personal growth?",
        "4. When you mess up, does she handle it maturely instead of just tearing you down?",
        "5. Does she speak respectfully of you and make you feel proud around other people?",
        "6. Even when you're apart, does she stay loyal and keep your trust intact?",
        "7. Does she actually care about the people who matter to you (like family or close friends)?",
        "8. When arguments happen, does she try to resolve things rather than just dragging them out?",
        "9. Does she value you for who you are, rather than what you have or your status?",
        "10. When you talk about the future, is she genuinely building that picture with you?"
    ]

    score = 0

    for i, q in enumerate(questions, 1):
        while True:
            answer = input(f"{q} (y/n): ").strip().lower()
            if answer in ['y', 'yes']:
                score += 1
                break
            elif answer in ['n', 'no']:
                break
            else:
                print("-> Just type 'y' for yes or 'n' for no, bro.")

    print("\n" + "=" * 60)
    print(f"ANALYSIS COMPLETE: You scored {score} out of 10")
    print("=" * 60)
    time.sleep(1)

    # Human-like breakdown and advice
    if score >= 9:
        print("Verdict: Real deal. Rare and genuine connection! ❤️")
        print("Takeaway: Hold onto this one. If she's riding with you through thick ")
        print("and thin, protect that bond, appreciate her, and keep growing together.")
        
    elif score >= 7:
        print("Verdict: Solid foundation, but needs a bit of fine-tuning. 💛")
        print("Takeaway: Things look good overall. There might be minor friction points, ")
        print("but that's normal. Talk things out openly and keep strengthening the trust.")
        
    elif score >= 5:
        print("Verdict: Mixed signals. Tread carefully. ⚠️")
        print("Takeaway: Honestly, it feels like it's drifting into habit or convenience rather ")
        print("than true depth. Take a step back, observe her actions over words, and don't force it.")
        
    else:
        print("Verdict: Major red flags. It's time to protect your peace. ❌")
        print("Takeaway: Look, if the effort is entirely one-sided and you're constantly second- ")
        print("guessing where you stand, staying will only drain you. Walk away with your self-respect ")
        print("intact. You deserve better than a one-way street.")
        
    print("=" * 60)

if __name__ == "__main__":
    analyze_relationship()
