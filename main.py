import math
def cosine(a,b):
    dot=sum(x*y for x,y in zip(a,b));na=math.sqrt(sum(x*x for x in a));nb=math.sqrt(sum(x*x for x in b));return dot/(na*nb) if na and nb else 0.0
def audit(original,transformed,attr_a,attr_b,score_drop=None):
    if len(attr_a)!=len(attr_b):raise ValueError('attribution shapes differ')
    result={'attribution_cosine':cosine(attr_a,attr_b),'l1_change':sum(abs(x-y) for x,y in zip(attr_a,attr_b))}
    if score_drop is not None:result['deletion_score_drop']=score_drop
    result['prediction_delta']=abs(original-transformed)
    return result
if __name__=='__main__':
    print(audit(.91,.90,[.5,.3,.2],[.48,.31,.21],score_drop=.37))
