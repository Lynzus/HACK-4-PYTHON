"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    x = list (result)
    for i in range(len(x)):
        if x[i]=="o":
            x[i]="0"
        elif x[i]=="i":
            x[i]="1"
        elif x[i]=="a":
            x[i]="@"
        else:
            x[i]=x[i].upper()
    return x
