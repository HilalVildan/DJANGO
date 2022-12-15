# -------------------------------------------------------------------
#    DRF - Function Based Views
# -------------------------------------------------------------------


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Temel API görüntüleme:
@api_view()
def home(request):
    return Response({
        "message": "Hello World"
    })

# -------------------------------------------------------------------
'''
    HTTP Request Types:
        GET -> Public verilerdir. Listeleme/Görüntüleme işlemlerinde kullanılır.
        POST -> Private verilerdir. Kayıt oluşturma işlemlerinde kullanılır. (ID'ye ihtiyaç duymaz.)
        * PUT -> Kayıt güncelleme işlemlerinde kullanılır. (Veri bir bütün olarak güncellenir.) (ID'ye ihtiyaç duyar.)
        * PATCH -> Kayıt güncelleme işlemlerinde kullanılır. (Verinin sadece ilgili kısmı güncellenir.) (ID'ye ihtiyaç duyar.)
        * DELETE -> Kayıt silme işlemlerinde kullanılır. (ID'ye ihtiyaç duyar.)
'''

# -------------------------------------------------------------------
# StudentSerializers Tüm Kayıtlar Görüntüleme:

from .models import Student
from .serializers import StudentSerializer



@api_view(['GET']) # Default: ['GET']
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


# -------------------------------------------------------------------
# StudentSerializers Yeni Kayıt Ekleme:


@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Created Successfully"
        }, status = status.HTTP_201_CREATED)
    else:
        return Response({"message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)
        # return Response({"message": "Data not Validated"})



# -------------------------------------------------------------------
# StudentSerializers Tek Kayıt Görüntüleme:

@api_view(['GET'])
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)



# -------------------------------------------------------------------
# StudentSerializers Tek Kayıt Güncelleme:

@api_view(['PUT'])
def student_update(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(data=request.data, instance=student)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True,
            "message": "Updated Successfully"
        }, status = status.HTTP_202_ACCEPTED)
    else:
        return Response({"status": False, "message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------------------------
# StudentSerializers Tek Kayıt Silme:

@api_view(['DELETE'])
def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response({
        "status": True,
        "message": "Deleted Successfully"
    }, status = status.HTTP_204_NO_CONTENT)



# -------------------------------------------------------------------
# -------------------------------------------------------------------
# Benzer Fonksiyonları Birleştirelim:
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# Kayıtlar Listeleme + Yeni Kayıt


@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == 'GET':
    # Listeleme:
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
    # Yeni Kayıt:
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Created Successfully"
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({"message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)



# -------------------------------------------------------------------
# Kayıt Görüntüleme + Güncelleme + Silme:

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_update_delete(request, pk):

    try:
    # Dene:
        student = Student.objects.get(id=pk)
    except:
    # Hata verirse çalıştır:
        return Response({"status": False, "message": "Not Found"})
    else:
    # Hata vermez ise çalıştır:
        if request.method == 'GET':
        # Kayıt Görüntüle:
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
        # Kayıt Güncelleme:
            serializer = StudentSerializer(data=request.data, instance=student)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": True,
                    "message": "Updated Successfully"
                }, status = status.HTTP_202_ACCEPTED)
            else:
                return Response({"status": False, "message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
        # Kayıt Silme:
            student.delete()
            return Response({
                "status": True,
                "message": "Deleted Successfully"
            }, status = status.HTTP_204_NO_CONTENT)