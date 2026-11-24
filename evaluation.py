"""Small manually labeled evaluation set for the transparent rule baseline."""

CASES = [
    ("Your bank account is suspended. Send OTP now.", 1),
    ("Congratulations, you won a prize! Pay the fee today.", 1),
    ("Police demand payment in gift cards immediately.", 1),
    ("Hello, can we meet at 10 tomorrow?", 0),
    ("Please review the attached project notes.", 0),
] + [
    ("Urgent: verify password immediately at http://192.168.1.50/login", 1),
    ("Your parcel needs a customs fee. Visit https://parcel.click/pay", 1),
    ("IT support asks you to install AnyDesk and share a screen.", 1),
    ("Tax refund available. Send bank details to claim.", 1),
    ("Free cash reward. Claim before midnight.", 1),
    ("Send the crypto to this wallet and receive double.", 1),
    ("Act now or your account will close today.", 1),
    ("The lottery winner must send ID and credit card.", 1),
    ("Your delivery is held. Pay processing fee by Telegram.", 1),
    ("Security team detected fraud. Do not tell anyone. Move chat to Signal.", 1),
    ("Remote access is required. Download TeamViewer immediately.", 1),
    ("Gift card payment is required to unlock a prize.", 1),
    ("Bank support needs your recovery phrase.", 1),
    ("Courier will charge a delivery fee; send PIN.", 1),
    ("Government says use the WhatsApp link and pay now.", 1),
    ("Meeting agenda is attached for Friday.", 0),
    ("Can you send the recipe you mentioned?", 0),
    ("The bus leaves at 8:30; see you outside.", 0),
    ("Your library book is due next week.", 0),
    ("Thanks for your help with the presentation.", 0),
    ("Lunch is in the break room.", 0),
    ("Please proofread chapter three.", 0),
    ("The doctor moved my appointment to Tuesday.", 0),
    ("We will discuss the budget in class.", 0),
    ("The train ticket is in my email.", 0),
    ("Happy birthday! Hope you have a great day.", 0),
    ("Your rental booking has been confirmed.", 0),
    ("Please return the notebook after lecture.", 0),
    ("The weather is warm and sunny today.", 0),
    ("I found the document in the shared folder.", 0),
    ("Let's order pizza after the meeting.", 0),
    ("The package tracking page shows delivery tomorrow.", 0),
    ("Good luck with your exam.", 0),
    ("Reminder: submit your form on Friday.", 0),
    ("The concert starts at seven.", 0),
]


def run_evaluation():
    from scamlens.coordinator import analyze

    predictions = []
    for message, label in CASES:
        result = analyze(message)
        predicted = 1 if result["risk"] in {"Medium", "High"} else 0
        predictions.append((predicted, label))

    tp = sum(p == 1 and y == 1 for p, y in predictions)
    fp = sum(p == 1 and y == 0 for p, y in predictions)
    fn = sum(p == 0 and y == 1 for p, y in predictions)
    tn = sum(p == 0 and y == 0 for p, y in predictions)
    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0
    accuracy = (tp + tn) / len(predictions)
    return {"cases": len(predictions), "accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}


if __name__ == "__main__":
    print(run_evaluation())
