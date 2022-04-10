from datetime import datetime

comment1 = {
    "Text": "What time?",
    "Name": "Ronny",
    "Username": "ronny56",
    "Picture": "Ronny.jpeg",
    "DateTime": datetime(2021, 7, 4, 19, 0, 0)
}

comment2 = {
    "Text": "At 8 pm, join me!",
    "Name": "Den",
    "Username": "denchick123",
    "Picture": "playful.png",
    "DateTime": datetime(2021, 7, 4, 19, 30, 0)
}

comment3 = {
    "Text": "Agree!",
    "Name": "Den",
    "Username": "denchick123",
    "Picture": "playful.png",
    "DateTime": datetime(2021, 7, 2, 18, 30, 0)
}

post1 = {
    "PostId": 1,
    "Text": "I can't wait to go to the park today",
    "Name": "Den",
    "Username": "denchick123",
    "Likes": ["ronny56"],
    "Comments": [comment1, comment2],
    "DateTime": datetime(2021, 7, 4, 18, 0, 0),
    "Picture": "playful.png"
}

post2 = {
    "PostId": 2,
    "Text": "Pet me rn",
    "Name": "Den",
    "Username": "denchick123",
    "Likes": [],
    "Comments": [],
    "DateTime": datetime(2021, 7, 3, 18, 0, 0),
    "Picture": "playful.png"
}

post3 = {
    "PostId": 3,
    "Text": "Treats are the best",
    "Name": "Ronny",
    "Username": "ronny56",
    "Likes": ["denchick123"],
    "Comments": [comment3],
    "DateTime": datetime(2021, 7, 2, 18, 0, 0),
    "Picture": "Ronny.jpeg"
}

test_posts = {
    1 : post1,
    2 : post2,
    3 : post3
}

den_posts = {
    1 : post1,
    2 : post2
}

ronny_posts = {
    3 : post3
}

den = {
    "Name": "Den",
    "Bio": "My name is Den and I'm a papillon. I'm a good boy and I like going to the country house.",
    "Username": "denchick123",
    "Picture": "playful.png",
    "Birthday": datetime(2013, 8, 13),
    "Posts": den_posts
}

ronny = {
    "Name": "Ronny",
    "Bio": "My name is Ronny, I like eating treats and wiggling my tail!",
    "Username": "ronny56",
    "Picture": "Ronny.jpeg",
    "Birthday": datetime(2015, 5, 15),
    "Posts": ronny_posts
}

dogs = {
    "denchick123" : den,
    "ronny56" : ronny
}

