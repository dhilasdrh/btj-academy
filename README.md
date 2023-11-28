# Simple Task

## 1. Buat Docker Image dari Aplikasi yang Dibuat

Pertama, buat **Dockerfile** pada direktori yang sama dengan file aplikasi yang dibuat, dengan isi:

    # gunakan base image Python 3.9
    FROM python:3.9
	
	# salin script python ke image
    COPY deskripsi_nilai.py .

	# tetapkan command default saat container berjalan
    CMD ["python", "deskripsi_nilai.py"]
Dockerfile ini menggunakan instruksi `FROM` untuk menggunakan image resmi Python 3.9 sebagai base Image, `COPY` untuk menyalin script Python `deskripsi_nilai.py` dari direktori lokal ke dalam image,  kemudian menggunakan instruksi `CMD` untuk menjalankan script tersebut sebagai command default saat container berjalan. 
 
   Setelah itu, tambahkan Dockerfile tersebut ke Git lalu push ke remote repository (GitHub).

    git add Dockerfile
	git commit -m “added Dockerfile”
	git push -u origin main

Lalu clone remote repository tersebut ke VM 

    git clone https://github.com/dhilasdrh/btj-academy.git

Setelah itu pindah/masuk ke direktori yang sudah di clone.

    cd btj-academy

Selanjutnya, buat docker image dalam direktori tersebut.

    docker build -t sampleapp:1.0.0 .

Perintah tersebut akan membangun sebuah Docker image dengan nama dan tag (label) **sampleapp:1.0.0** dari Dockerfile yang berada di direktori saat ini. **sampleapp** adalah nama repository, dan **1.0.0** adalah tag nya.

Terakhir, pastikan docker image telah berhasil dibuat.

    docker images

Ini akan menampilkan seluruh docker images pada container tersebut

## 2. Jalankan Docker Image pada Port 8081

Untuk menjalankan image tersebut pada port 8081, jalankan perintah:

    docker run -it -d --expose 8081 --name "sample_app" sampleapp:1.0.0
Keterangan:
-   **docker run** → perintah untuk jalankan container dari sebuah image.
-   **-it** →  opsi **-i (interactive)** dan **-t (tty)**, untuk membuat container berjalan dalam mode interaktif dan terhubung ke terminal.
-   **-d** → opsi **-d (detach)** untuk menjalankan container dalam mode latar belakang (background) dan tidak akan menempati terminal.
-   **--expose 8081** → **--expose** untuk mengekspos (membuka) port tertentu dari container. Dalam hal ini, container akan mengekspos port **8081** ke host.
-   **--name "sample_app"** → **–name** digunakan untuk memberi nama pada container yang berjalan. Dalam hal ini, namanya adalah **"sample_app"**.
-   **sampleapp:1.0.0** → nama dan versi dari image Docker yang akan digunakan untuk membuat container.
## 3. IP Container whoami

Untuk mengetahui IP dari container, gunakan perintah **docker inspect <nama_container>**.

    docker inspect whoami
Outputnya akan berupa JSON yang mencakup berbagai informasi tentang container tersebut, termasuk konfigurasi jaringan dan IP Addrress.

Di bagian **"Networks"**, dapat terlihat IP Address container whoami adalah **172.17.0.2**

Selain perintah di atas, IP Address container juga dapat diketahui dengan perintah berikut:

    docker inspect -f '{{ .NetworkSettings.IPAddress }}' whoami
opsi `-f` atau `--format` digunakan untuk menentukan format output dari perintah docker inspect. Dalam hal ini, kita menggunakan format `{{ .NetworkSettings.IPAddress }}` yang akan secara spesifik mengekstrak informasi mengenai IP Address dari container `whoami`.

## 4. Isi File Tersembunyi dari Docker Container whoami
Pertama, inspeksi isi container whoami menggunakan perintah: 

    docker inspect whoami 

Berdasarkan output dari perintah tersebut, dapat terlihat bahwa container whoami menggunakan volume mounting dengan konfigurasi berikut:

    "Mounts": [
    	{
    		"Type": "bind",
    		"Source": "/home/local/.docker",
    		"Destination": "/tmp/system",
    		"Mode": "",
    		"RW": true,
    		"Propagation": "rprivate"
    	}
    ],
Volume mounting dilakukan dari `/home/local/.docker` pada host ke `/tmp/system` di dalam container dengan tipe binding (bind type). Artinya, direktori `/home/local/.docker` pada host akan di-mount (dibagikan/dikaitkan) ke dalam container **whoami** di lokasi `/tmp/system`.

Untuk mengetahui isi dari file yang tersembunyi dari container tersebut, cek dulu seluruh file yang terdapat dalam direktori `/tmp/system`, termasuk file tersembunyi.

    docker exec whoami ls -la /tmp/system
outputnya menunjukkan ada file bernama **whoami** dalam direktori tersebut. Selanjutnya, buka isi dari file whoami dengan perintah:

    docker exec whoami cat /tmp/system/whoami
Hasilnya adalah: 
`Oofooni1eeb9aengol3feekiph6fieve`

## 5. Image yang digunakan pada Container whoami

Untuk mengetahui docker image yang digunakan pada container whoami, gunakan perintah:

    docker ps
Ini akan memberikan informasi seperti container id, image, command, status, port yang di-mapping, dan sebagainya.

Berdasarkan output perintah tersebut, dapat terlihat nama Image dari container whoami adalah:
`secret:aequaix9De6dii1ay4HeeWai2obie6Ei`

Artinya, container **whoami** menggunakan Docker image dengan nama `secret` dan tag `aequaix9De6dii1ay4HeeWai2obie6Ei`.

Selain perintah di atas, nama Image yang digunakan pada container juga dapat diketahui dengan perintah berikut.

    docker inspect -f '{{ .Config.Image }}' whoami
opsi `-f` digunakan untuk memformat output sesuai dengan format yang ditentukan oleh template Go. Dalam hal ini, template Go yang digunakan adalah `{{ .Config.Image }}`, berarti secara spesifik ingin mengekstrak informasi tentang nama Docker image dari konfigurasi container dengan nama `whoami`.
