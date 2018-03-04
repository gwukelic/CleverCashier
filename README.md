# CleverCashier

Updated: 3/4/2018

The drive thru system is archaic. We think the system could be improved by
incorporating smart speaker technology (e.g. Amazon Echo) and computer vision.
We built this tool using Python, openCV, ASK (Alexa Skills Kit), and AWS (Amazon
Web Services). Specifically, we used a Python and Clarifai APIs to begin an order.
We used AWS Lambda and DynamoDB to process the order.

Currently, only one item can be ordered at a time. Variations of sizes, quantities,
and menu items (burgers, fries, sodas, ice creams, etc.) can be requested.
