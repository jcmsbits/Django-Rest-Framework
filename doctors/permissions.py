from rest_framework import permissions

class IsDoctor(
    permissions.BasePermission
):
    # Con has_permission que tenga a acceso a todos los objectos
    # con 
    def has_permission(self, request, view):
        return request.user.groups.filter(name = "doctors").exists()
    
    # Con has_object_permission le específicamos que tenga acceso solo a los
    # objetos que creó
    # def has_object_permission(self, request, view, obj):
    #     return super().has_object_permission(request, view, obj)