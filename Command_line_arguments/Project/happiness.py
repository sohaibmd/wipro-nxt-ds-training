import sys

def calculate_happiness(likes_str, dislikes_str, given_str):
    likes = set(likes_str.split('-'))
    dislikes = set(dislikes_str.split('-'))
    given = given_str.split('-')
    
    happiness = 0
    for num in given:
        if num in likes:
            happiness += 1
        elif num in dislikes:
            happiness -= 1
    return happiness

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python happiness.py <likes> <dislikes> <given>")
    else:
        likes = sys.argv[1]
        dislikes = sys.argv[2]
        given = sys.argv[3]
        result = calculate_happiness(likes, dislikes, given)
        print(result)
