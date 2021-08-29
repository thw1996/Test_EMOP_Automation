test = {"step": "4", "talkContent": "5", "ordernum": "6", "isRead": "7"}
a = test["step"]
production1 = [("step"),("talkContent"),("ordernum"),("isRead")]
production = [{"step": "4"}, {"talkContent": "5"}, {"ordernum": "6"}, {"isRead": "7"}]
test = [{"step": "4"}, {"talkContent": "5"}, {"ordernum": "6"}, {"isRead": "7"}]
# for j in (production1):
#     print(j)
for p,t,j in zip(production,test,production1):
    print(j)
    print(p)
    print(t)

