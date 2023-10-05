from fastapi import FastAPI
from typing import List

app = FastAPI()

# Sample data (replace with your actual data)
cards = ["Card 1", "Card 2", "Card 3"]
votes = [0, 0, 0]
current_card_index = 0


@app.get("/getList")
def get_list():
    return cards


@app.put("/upvote/{card_index}")
def upvote(card_index: int):
    global votes
    if 0 <= card_index < len(cards):
        votes[card_index] += 1
        return {"message": "Upvoted successfully."}
    else:
        return {"message": "Invalid card index."}


@app.put("/downvote/{card_index}")
def downvote(card_index: int):
    global votes
    if 0 <= card_index < len(cards):
        votes[card_index] -= 1
        return {"message": "Downvoted successfully."}
    else:
        return {"message": "Invalid card index."}


@app.get("/nextCard")
def next_card():
    global current_card_index
    current_card_index = (current_card_index + 1) % len(cards)
    return {"next_card": cards[current_card_index]}

"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
