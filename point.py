def bating(run=0 , four=0 , six=0 , balls=0) :
    pt=int(run/2)
    sr=0
    if balls >0:
        sr=run/balls
    
    if (run > 99) :
        pt=pt+15
    else:
        if(run >49):
            pt=pt+5
        
    if(sr>1):
        pt=pt+4
    elif(sr>0.80):
        pt=pt+2
    
    pt = pt + four + six*2
    return pt

def bowling(wicket=0,run=0,over=0) :
    pt=10*wicket
    
    economy=100
    if over>0 :
        economy=run/over
    if(wicket>5 or wicket==5):
        pt=pt+15
    elif(wicket>3 or wicket==3):
        pt=pt+5
    
    
    if((economy>3.5) and (economy <4.5) or economy==4.5) :
        pt = pt+ 4

    if(economy>2 and economy < 3.5 or economy==3.5 ):
        pt=pt+7
    
    if(economy<2):
        pt=pt+10
    
    return pt

def point(btrun=0,four=0,six=0,balls=0, witcket=0 , over=0,bwrun=0 ,feilding=0) :
    bt = bating(btrun , four , six , balls)
    bw = bowling(witcket,bwrun,over)
    pt=bt+bw+feilding*10
    # print("batting ={} balling ={}".format(bt,bw))
    return pt




# z = point(112,10,0,119)
# p= point(witcket=3,bwrun=34,over=10)
# print(p)