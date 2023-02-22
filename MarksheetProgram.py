p,ch,m,h,e = 26,67,80,81,89
gm=0
sub=""
dist=""
if  (p>=0 and p<=100) and (ch>=0 and ch<=100) and (m>=0 and m<=100)
and (h>=0 and h<=100) and (e>=0 and e<=100):
    c=0
       
    if p<33:
       c = c+1
       gm=p
       sub = sub + " PHY "
    if ch<33:
        c = c+1
        gm=ch
        sub = sub + " CHEM "
    if m<33:
        c = c+1
        gm=m
        sub = sub + " Maths "
    if h<33:
        c = c+1
        gm=h
        sub = sub + " HIN "
    if e<33:
        c = c+1
        gm=e
        sub = sub + " ENG "

    if c==0 or (c==1 and gm>=28):
        if p>=75:
           dist = dist + " PHY "
        if ch>=75:
           dist = dist + " CHEM "
        if m>=75:
           dist = dist + " MATH "
        if h>=75:
           dist = dist + " HINDI "
        if e>=75:
           dist = dist + " ENGLISH " 
        if c==0:
           per = (p+ch+m+h+e)/5
        else:
           per = (p+ch+m+h+e+(33-gm))/5
           print("Pass By Grace in ",sub)
        if per>=33 and per<45:
            print("pass with third division and percenatge is ",per)
        elif per<60:
            print("pass with second division percenatge is ",per)
        else:
            print("pass with first division percenatge is ",per)
        if dist!="":
            print("Distinction Subjects are ",dist)
            
    elif c==1:
        print("suppl in ",sub)
    else:
        print("fail in ",sub)
        
        
else:
    print("All subject marks should be between 0 to 100")
