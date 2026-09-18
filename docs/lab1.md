# Лабораторийн ажил №1 — Хөгжүүлэлтийн орчин ба Git

## 1. Багийн бүрэлдэхүүн, үүрэг

| Гишүүн | Scrum үүрэг | Хариуцах ажил |
|---|---|---|
| Д.Ууганбаяр | Product Owner, Developer | Шаардлага тодорхойлох, Backlog-ийн эрэмбэ, код бичих |
| [2-р гишүүний нэр] | Scrum Master, Developer | Sprint-ийн уулзалт зохион байгуулах, саад арилгах, код бичих |

Баг 2 хүнтэй тул Development Team-д хоёулаа багтана.

## 2. Хөгжүүлэлтийн орчин

| Хэрэгсэл | Хувилбар | Төлөв |
|---|---|---|
| Visual Studio Code | 1.137 | суусан |
| Git | 2.50.1 | суусан |
| GitLens | 19.2.0 | суусан |
| Prettier | — | суусан |
| Python extension | — | суусан |

Git суусныг шалгах:

```bash
git --version
```

## 3. GitHub бүртгэл, repository

1. github.com дээр `Uuganaaa12` бүртгэлээрээ нэвтэрнэ.
2. **New repository** дарж `suh-burtgel` нэрээр үүсгэнэ.
3. **Public** сонгоно.
4. *Initialize this repository with a README* сонголтыг **сонгохгүй**.

## 4. Clone, commit, push

```bash
git clone https://github.com/Uuganaaa12/suh-burtgel.git
cd suh-burtgel
# README.md файлыг үүсгэж агуулгыг бичнэ
git add README.md
git commit -m "Анхны README файлыг нэмэв"
git push origin main
```

## 5. Үр дүн

- Repository: https://github.com/Uuganaaa12/suh-burtgel
- README.md файл GitHub дээр харагдаж байна.
- Commits хэсэгт анхны commit бүртгэгдсэн.

Commit: `9eb83c3` — «Лаб 1: төслийн README болон баримт бичиг»

*(Дэлгэцийн зургийг энд хавсаргана: repo-ийн нүүр хуудас, Commits жагсаалт.)*

## Гүйцэтгэлийн шалгуур

- [x] VS Code, Git суурилуулсан
- [x] GitLens суулгасан
- [x] GitHub бүртгэл үүсгэсэн (Uuganaaa12)
- [x] GitHub дээр repository үүсгэсэн
- [x] Repository-г локал компьютер дээр clone хийсэн
- [x] README.md файл үүсгэсэн
- [x] git add, git commit, git push хэрэглэсэн
- [x] GitHub дээр файл, commit харагдаж байна
- [ ] Багийн гишүүдийн үүргийг тодорхойлсон
