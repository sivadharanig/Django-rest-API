from django.shortcuts import render
from rest_framework.views import APIView
from .models import Catagerymodule
from rest_framework.response  import Response
from .serializers import CatagerySerilizer
from django.shortcuts import get_object_or_404
# Create your views here.
class catageryview(APIView):
    # def get(self,request):
    #     data=Catagerymodule.objects.values('name').all()
    #     datalist=[{"name":[i["name"] for i in data]}]
    #     return Response(datalist)
    def get(self,request,*args, **kwargs):
        # if pk avilable we will get the perticular date
        # if self.get_object('pk')
        if kwargs.get('pk') !=None:
            data=Catagerymodule.objects.filter(id=kwargs.get('pk')).first()
            Serdata=CatagerySerilizer(data)
        # default
        else:
            data=Catagerymodule.objects.all()
            Serdata=CatagerySerilizer(data,many=True)
        # print(Serdata.data)
        #print (Serdata.error)  
        return Response(Serdata.data)
    def post(self,request):
        dataserilalizes=CatagerySerilizer(data=request.data)
        if dataserilalizes.is_valid():
           dataserilalizes.save()
           return Response(dataserilalizes.data)
        else:
            return Response(dataserilalizes.errors)
        
    def put(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        #solution 1
        category = get_object_or_404(Catagerymodule, id=pk)
        # If resource doesn't exist, create a new one
        serializer =CatagerySerilizer(data=request.data)
        # Update the existing resource
        # serializer =CatagerySerilizer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":f"{serializer.data}"})
        else:
            return Response({"error":f"{serializer.errors}"})
        #Solution 2
        # datacatagery=Catagerymodule.objects.filter(id=pk).first()
        # if datacatagery ==None:
        #      return Response({"status":404,"Detais":f"detail Not found id {pk}"})
        # print(datacatagery.__dict__)
        # print(request.data)
        # Serialize=CatagerySerilizer(datacatagery,request.data)
        # if Serialize.is_valid():
        #     Serialize.save()
        #     return Response({"data":f"{Serialize.data}"})
        # else:
        #     return Response({"error":f"{Serialize.errors}"})
    def patch(self,request,*args, **kwargs):
        pk=kwargs.get('pk')
        Requestdata=get_object_or_404(Catagerymodule,id=pk)
        serilizerdata=CatagerySerilizer(Requestdata,data=request.data,partial=True)
        if serilizerdata.is_valid():
            serilizerdata.save()
            return Response({"data":serilizerdata.data})
        else:
            return Response({"data":serilizerdata.errors})
        


class catageryviewversion(APIView):
    # def get(self,request):
    #     data=Catagerymodule.objects.values('name').all()
    #     datalist=[{"name":[i["name"] for i in data]}]
    #     return Response(datalist)
    def get(self,request,*args, **kwargs):
        # if pk avilable we will get the perticular date
        # if kwargs.get('pk') !=None:
        data=Catagerymodule.objects.filter(id=kwargs.get('pk')).first()
        Serdata=CatagerySerilizer(data)
        # default
        # else:
        #     data=Catagerymodule.objects.all()
        #     Serdata=CatagerySerilizer(data,many=True)
        # print(Serdata.data)
        #print (Serdata.error)  
        return Response(Serdata.data)