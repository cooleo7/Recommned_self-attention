from .base import BaseModel
from meantime.utils import all_subclasses
from meantime.utils import import_all_subclasses
import_all_subclasses(__file__, __name__, BaseModel)
from .transformer_models.bert import BertModel   #추가
from .transformer_models.sas import SASModel   #추가
from .transformer_models.meantime import MeantimeModel   #추가
from .transformer_models.tisas import TiSasModel   #추가

MODELS = {c.code():c
          for c in all_subclasses(BaseModel)
          if c.code() is not None}

print("111")
print(BaseModel)
print(all_subclasses(BaseModel))
print(MODELS)

#MODELS = {'bert':meantime.models.marank.MARankModel} -> meantime is not defined

#MODELS = {'bert':<class 'meantime.models.marank.MARankModel'>} MODELS = {'bert':<class 'meantime.models.marank.MARankModel'>}
#                 ^
#SyntaxError: invalid syntax

#MODELS = {'bert':class transformer_models.bert.BertModel}
#                     ^
#SyntaxError: invalid syntax

#MODELS = {'bert':transformer_models.bert.BertModel} 
#          'marank': <class 'meantime.models.marank.MARankModel'>,
#          'marank': <class 'meantime.models.marank.MARankModel'>,
#          'marank': <class 'meantime.models.marank.MARankModel'>,
#          'marank': <class 'meantime.models.marank.MARankModel'>,
#          'marank': <class 'meantime.models.marank.MARankModel'>}}
#print("111")
#print(BaseModel)
#print(all_subclasses(BaseModel))
#print(MODELS)

def model_factory(args):
    print("222")
    print(args)
    print(args.model_code)
    #model = MODELS[args.model_code] #삭제
    #model = MODELS['bert'] #수정
    #print(model)
    #return model(args)  #삭제
    #return BertModel(args)  #모델별로 수정적용
    #return SASModel(args)   #모델별로 수정적용
    if args.model_code == 'bert':
        return BertModel(args)  #모델별로 수정적용
    if args.model_code == 'sas':
        return SASModel(args)  #모델별로 수정적용
    if args.model_code == 'meantime':
        return MeantimeModel(args)  #모델별로 수정적용
    if args.model_code == 'tisas':
        return TiSasModel(args)  #모델별로 수정적용
    


