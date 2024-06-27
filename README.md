# siwp2005-final-project
# Nama Kelompok 
*Adrielle Bintang Pratama - 422023021
*Billy Michael Junus Saija - 422023018
*Kevin Divra David Sebasti Nababan - 422023023
*Yobel Kimtoputra - 422023001

## Swagger UI
Contoh Implementasi Backend : [openapi.yaml](./backend/app/static/openapi.yaml).


### Quick start

- To start and build the development flask backend:
```
docker compose -f docker-compose.yaml up --build -d
```
Note: `docker compose` command is used in `Compose V2`. Supoosedly your version is `Compose V1` replace `docker compose` with `docker-compose`

After successful run the dev server, you will be able to see all containers are running 
```shell
docker ps
```
check specific container
```shell
docker ps --filter name="name of the container" 
```
- To stop service
```
docker compose -f docker-compose.yaml down
```
*specify `-v` to remove the mongodb volume*

- To remove all container
```
docker system prune
```

### Tech stack
- Flask
- MongoDB
- Docker  

References
* flask_mongoengine -> MongoDB connector ([docs](https://docs.mongoengine.org/# "docs"))
  * flask_jwt_extended -> JWT Token
- MongoDB ([docs](https://github.com/docker-library/docs/tree/master/mongo "docs"))

- Marshmallow -> Schema Validator ([docs](https://marshmallow.readthedocs.io/en/stable/index.html "docs"))
- Docker


### Debugging
Build Development
```shell
docker compose -f docker-compose.yaml up --build -d
```
Check Countainer 
```shell
docker ps
```
Debug via docker logs
```shell
docker logs 'container name'
```

## Membuat PORTAL UKRIDA 
Kami membuat sistem Portal Ukrida yang di dalamnya terdapat beberapa fitur

## PORTAL UKRIDA
## 1. Requirement Analysis
## A. Functional Requirement Portal Ukrida
•	Autentikasi USER:
-	USER harus dapat melakukan login ke portal menggunakan kredensial yang valid, seperti Nama dan kata sandi.
-	Setelah login, USER memiliki akses ke fitur-fitur yang tersedia.

•	Pencarian Informasi:
-	USER dapat mencari informasi terkait akademik, seperti nilai dari mata kuliah tersebut.
-	Sistem harus menyediakan hasil pencarian yang relevan dan akurat

•	Logout:
-	USER harus memiliki opsi untuk logout dari portal saat selesai menggunakan.

## B. Non-Functional Requirement Portal Ukrida
•	Keamanan:
-	Portal harus memiliki tingkat keamanan yang tinggi untuk melindungi data sensitif pengguna, seperti informasi pribadi dan kredensial login.
-	Sistem harus menerapkan praktik-praktik keamanan terbaik, seperti manajemen kata sandi yang aman dan penggunaan mekanisme otentikasi dua faktor.

•	Ketersediaan:
-	Portal harus tersedia untuk digunakan sepanjang waktu, kecuali pada saat jadwal pemeliharaan yang dijadwalkan.
-	Downtime portal harus minimal dan harus ada strategi pemulihan bencana yang disiapkan untuk mengatasi kegagalan sistem yang tak terduga.

•	Kinerja:
-	Portal harus responsif dan dapat menangani beban yang tinggi tanpa mengalami penurunan kinerja yang signifikan.
-	Waktu respons untuk setiap operasi dalam portal, seperti login dan pencarian informasi, harus cepat dan sesuai dengan harapan pengguna.

•	Usability (Kemudahan Penggunaan):
-	Antarmuka pengguna harus dirancang dengan baik dan mudah digunakan oleh USER dari berbagai latar belakang.
-	Sistem harus menyediakan bantuan kontekstual dan dokumentasi yang jelas untuk membantu pengguna dalam menggunakan fitur-fitur portal dengan efektif.

•	Skalabilitas:
-	Arsitektur portal harus dirancang dengan baik untuk mendukung pertumbuhan jumlah pengguna dan volume data yang meningkat.
-	Sistem harus dapat dengan mudah berkembang seiring waktu tanpa mengorbankan kinerja atau ketersediaan.

•	Mudah Pemeliharaan:
-	Kode portal harus bersih, terdokumentasi dengan baik, dan mudah dipelihara untuk memfasilitasi pengembangan dan pemeliharaan selanjutnya.
-	Sistem harus memanfaatkan teknologi dan alat pemantauan yang tepat untuk memudahkan pemantauan kesehatan portal dan deteksi masalah yang mungkin timbul.

•	Kompatibilitas:
-	Portal harus kompatibel dengan berbagai perangkat dan platform, termasuk komputer desktop, laptop, dan perangkat mobile.
-	Antarmuka pengguna harus dirancang responsif agar dapat disesuaikan dengan berbagai ukuran layar dan resolusi.

## 2. Usecase Stories 
A. Login
Aktor: USER
Deskripsi: USER dapat melakukan login ke dalam portal sistem USER.
Langkah-langkah:

1.	USER membuka portal sistem USER.
2.	USER memasukkan Nama dan kata sandi.
3.	Sistem memvalidasi kredensial USER.
4.	Jika kredensial valid, sistem mengizinkan akses ke fitur-fitur portal.
5.	Jika kredensial tidak valid, sistem menampilkan pesan kesalahan.

B. Menampilkan Menu Sistem
Aktor: USER
Deskripsi: USER dapat melihat menu sistem untuk memilih sistem yang ingin diakses.
Langkah-langkah:
1.	USER berhasil login ke dalam portal sistem USER.
2.	Sistem menampilkan menu sistem yang tersedia.
3.	USER memilih salah satu opsi sistem yang ingin diakses.

C. Menjalankan SISFO
Aktor: USER
Deskripsi: USER dapat menjalankan SISFO (Sistem Informasi Akademik) untuk mengakses informasi akademik.
Langkah-langkah:
1.	USER memilih opsi SISFO dari menu sistem.
2.	Sistem membuka aplikasi SISFO.
3.	USER dapat mengakses informasi akademik seperti jadwal kuliah, nilai, dan lain-lain.

D.  Logout
Aktor: USER
Deskripsi: USER dapat keluar dari portal sistem USER.
Langkah-langkah:
1.	USER memilih opsi logout dari menu sistem.
2.	Sistem menghapus sesi login USER.
3.	USER keluar dari portal sistem dan kembali ke halaman login.

E. Menampilkan Informasi USER
Aktor: USER
Deskripsi: USER dapat melihat informasi pribadi mereka yang tersimpan dalam sistem.
Langkah-langkah:
1.	USER berhasil login ke dalam portal sistem USER.
2.	USER memilih opsi untuk melihat informasi pribadi.
3.	Sistem menampilkan informasi pribadi USER seperti nama, NIM, dan email.

## 3. Usecase