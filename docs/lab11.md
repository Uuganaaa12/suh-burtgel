# Лабораторийн ажил №11 — Статик шинжилгээ, эмзэг байдал илрүүлэх

Хичээл: Программ хангамж хөгжүүлэлтийн процесс (12-р долоо хоног)\
Төсөл: СӨХ-ийн сууц, машин, зогсоолын бүртгэлийн систем\
Баг: Д.Ууганбаяр (Product Owner), Ц.Номунзаяа (Scrum Master)\
Repository: <https://github.com/Uuganaaa12/suh-burtgel>

## 1. Зорилго

- Linter тохируулж, кодын стилийн алдааг автоматаар илрүүлэх.
- Dependency scanning ашиглан гуравдагч сангийн эмзэг байдлыг олох.
- Илэрсэн асуудлыг ач холбогдлоор нь ангилж засах.

Төсөл Python дээр тул ESLint-ийн оронд **pylint 4.1.4**, `npm audit`-ын оронд **pip-audit 2.10.1** ашиглав. Хоёулаа ижил үүрэгтэй: эхнийх нь кодыг, хоёр дахь нь хамаарлыг шалгана.

## 2. Linter

### 2.1. Тохиргоо (`.pylintrc`)

pylint-ийн анхдагч дүрмийн багцыг суурь болгож, хоёрыг л өөрчлөв:

- `no-docstring-rgx = ^(_|test_)`: `test_` функцын нэр өөрөө юуг шалгахыг тайлбарладаг (`test_negative_amount_is_rejected`) тул docstring шаардахгүй. Туслах функц, модульд docstring шаардсаар байна.
- `max-line-length = 120`: багийн тохиролцсон мөрийн урт.

### 2.2. Өмнө / дараа

| | Өмнө | Дараа |
|---|---|---|
| Оноо | 8.00/10 | 10.00/10 |
| Анхааруулга | 23 | 0 |

Өмнөх гаралтын хэсэг:

```
************* Module test_queue
tests/test_queue.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_queue.py:8:0: C0116: Missing function or method docstring (missing-function-docstring)
...
************* Module test_late_fee
tests/test_late_fee.py:1:0: C0114: Missing module docstring (missing-module-docstring)
...
Your code has been rated at 8.00/10
```

Дараах гаралт:

```
Your code has been rated at 10.00/10 (previous run: 9.83/10, +0.17)
```

### 2.3. Засварууд

| № | Асуудал | Хаана | Засвар |
|---|---|---|---|
| 1 | C0114 модулийн docstring алга | `tests/test_queue.py` | Модулийн тайлбар нэмэв |
| 2 | C0114 модулийн docstring алга | `tests/test_late_fee.py` | Модулийн тайлбар нэмэв |
| 3 | C0116 туслах функцын docstring алга | `tests/test_queue.py: req()` | Docstring нэмэв |
| 4 | C0116 туслах функцын docstring алга | `tests/test_queue.py: ids()` | Docstring нэмэв |
| 5-23 | C0116 тест функцын docstring алга (19) | `tests/*.py` | `.pylintrc`-ийн `no-docstring-rgx` (2.1-д үндэслэл) |

`suh/` доторх үндсэн кодонд анхааруулга гараагүй.

## 3. Dependency scan (`pip-audit`)

```
$ pip-audit -r requirements.txt
Found 2 known vulnerabilities in 1 package
Name   Version ID              Fix Versions
------ ------- --------------- ------------
pytest 8.3.3   PYSEC-2026-1845 9.0.3
```

| Сан | Эмзэг байдал | Тайлбар | CVSS 3.1 | Ангилал | Шийдвэр |
|---|---|---|---|---|---|
| pytest 8.3.3 | PYSEC-2026-1845 (CVE-2025-71176, GHSA-6w46-j5rx-g56g) | UNIX дээр `/tmp/pytest-of-{user}` хавтсыг ашигладаг тул тухайн компьютерын өөр хэрэглэгч үйлчилгээг зогсоох эсвэл эрх олж авах боломжтой | AV:L/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:L, суурь оноо 6.8 | **Medium** | 9.0.3 болгож шинэчлэв |

Critical, High ангиллын эмзэг байдал илрээгүй. Энэ эмзэг байдал зөвхөн тухайн компьютерын хэрэглэгчээс (local) халддаг, pytest зөвхөн хөгжүүлэлт, CI-д ашиглагддаг тул эрсдэл бага. Гэхдээ засвар гарсан тул шууд шинэчлэв. Шинэчилсний дараа:

```
$ pip-audit -r requirements.txt
No known vulnerabilities found
$ pytest -q
24 passed
```

Эх сурвалж: <https://osv.dev/vulnerability/PYSEC-2026-1845>, <https://nvd.nist.gov/vuln/detail/CVE-2025-71176>

## 4. CI-д нэгтгэх

`.github/workflows/ci.yml`-д тестийн өмнө хоёр алхам нэмэв. Аль нэг нь алдаа олбол pipeline улаан болж, тест ажиллахгүй.

```yaml
      - name: Lint (pylint)
        run: pylint suh tests

      - name: Dependency scan (pip-audit)
        run: pip-audit -r requirements.txt

      - name: Test
        run: pytest -v
```

`requirements.txt`: `pytest==9.0.3`, `pylint==4.1.4`, `pip-audit==2.10.1`.
