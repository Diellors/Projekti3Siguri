# Komunikimi i Sigurt Klient-Server (TCP) me Kriptim dhe Nënshkrim Digjital (X.509)

Ky projekt realizon një aplikacion të sigurt të komunikimit **Client-Server** përmes protokollit **TCP** në gjuhën programuese **Python**. 
Mesazhet që dërgohen nga klienti te serveri transmetohen të kriptuara dhe të nënshkruara në formë digjitale, duke përdorur parametrat e lexuar nga certifikatat digjitale.

---

## 🔒 Karakteristikat e Sigurisë

Projekti zbaton tri shtyllat kryesore të sigurisë së informacionit:
1. **Fshehtësia (Confidentiality):** Mesazhi kriptohet me algoritmin asimetrik **RSA (PKCS1-OAEP)** duke përdorur çelësin publik të serverit të nxjerrë nga certifikata e tij. Vetëm serveri mund ta dekriptojë atë me çelësin e tij privat.
2. **Integriteti (Integrity):** Çdo mesazh pajiset me një nënshkrim digjital **RSA (PKCS1-15)** të bazuar në hash-in **SHA-256**. Nëse mesazhi manipulohet rrugës, serveri e dikton menjëherë sepse verifikimi i nënshkrimit dështon.
3. **Autenticiteti (Authenticity):** Serveri përdor certifikatën X.509 të klientit (`client_cert.crt`) për të verifikuar nënshkrimin, duke garantuar që mesazhi ka ardhur me të vërtetë nga klienti i autorizuar.

---

## 🛠️ Teknologjitë e Përdorura

* **Gjuha:** Python 3.10+
* **Libraria Kriptografike:** `pycryptodome` (për RSA, SHA-256, nënshkrimet dhe menaxhimin e certifikatave)
* **Libraria e Rrjetit:** `socket` (për komunikimin e pastër TCP)

---
