from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CodeSerializer
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import os

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
@authentication_classes([TokenAuthentication])
def compile_code(request):
    serializer = CodeSerializer(data=request.data)
    if serializer.is_valid():
        # Lakukan proses kompilasi/eksekusi kode di sini
        # Cek tipe bahasa yang digunakan
        language = serializer.validated_data['language']
        code = serializer.validated_data['code']
        
        if language == 'python':
            # Proses kode Python
            import subprocess
            process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            
        elif language == 'php':
            # Proses kode PHP
            if "<?php?>" in code:
                return Response("Mohon tidak menggunakan sintaks '<?php?>', namun harap lagsung isi dengan kode php untuk kompilasi", status=400)
            import subprocess
            current_dir = os.path.dirname(os.path.abspath(__file__))
            compiler_path = os.path.join(current_dir, '../compilers/php/php.exe')
            process = subprocess.Popen([compiler_path, '-r', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            
            # Jika menggunakan file PHP, ganti perintah menjadi:
            # php_file_path = os.path.join(current_dir, 'path/ke/file.php')
            # process = subprocess.Popen(['php', php_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif language == 'node':
            # Proses kode Node.js
            import subprocess
            process = subprocess.Popen(['node', '-e', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
        elif language == 'node':
            # Proses kode Node.js
            import subprocess
            process = subprocess.Popen(['node', '-e', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
        elif language == 'node':
            # Proses kode Node.js
            import subprocess
            process = subprocess.Popen(['node', '-e', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
        elif language == 'node':
            # Proses kode Node.js
            import subprocess
            process = subprocess.Popen(['node', '-e', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
        else:
            return Response("Unsupported language", status=400)
        
        # Ubah output menjadi string dan kirim sebagai respons
        output = output.decode('utf-8')
        return Response(output)
    
    return Response(serializer.errors, status=400)
