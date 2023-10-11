"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    x = list (result)
    for i in range(len(x)):
        if x[i]=="o":
            x[i]="0"
        elif x[i]=="i":
            x[i]="1"
        elif x[i]=="a":
            x[i]="@"
    return ''.join(x)
print(fn_hack_5())