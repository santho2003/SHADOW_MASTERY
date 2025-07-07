def scoring(data):

    data["exercise"] = data["exercise"] / 60
    data["study"] = data["study"] / 60
    prod_score = 0
    prod_score += 60 if data["sleep"] >= 6 else 10 * data["sleep"]
    prod_score += 10 if data["coding"] >= 1 else 10 * data["coding"]
    prod_score += 20 if data["exercise"] >= 0.5 else 20 * data["exercise"]
    prod_score += 10 if data["study"] >= 0.6 else 10 * data["study"]
    
    return prod_score

def verdict(data):
    verdict = ""
    verdict += "Need more sleep to recover." if data["sleep"] < 6 else ""
    verdict += "Still have to power to solve more." if data["coding"] < 1 else ""
    verdict += "Less than 30 mins of study is not enough to grow." if data["study"] < 0.6 else ""

    return verdict