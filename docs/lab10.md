# Лабораторийн ажил №10 — Автомат тест бичих, CI Pipeline-д холбох

Хичээл: Программ хангамж хөгжүүлэлтийн процесс (11-р долоо хоног)\
Төсөл: СӨХ-ийн сууц, машин, зогсоолын бүртгэлийн систем\
Баг: Д.Ууганбаяр (Product Owner), Ц.Номунзаяа (Scrum Master)\
Repository: <https://github.com/Uuganaaa12/suh-burtgel>

## 1. Зорилго

- Arrange-Act-Assert (AAA) зарчмаар unit тест бичих.
- Mock ашиглан гадаад хамаарлыг (өгөгдлийн сан) тусгаарлах.
- Тестээ Лаб 7-ийн CI pipeline-д нэгтгэх.

## 2. Тестлэх функц

Багшийн жишээ `calculateTotal()`-тэй дүйцэх функц болгон сарын нэхэмжлэхийн нийт дүнг сонгов (`suh/billing.py`):

- `invoice_total(fee, rent, days_overdue, daily_rate)`: хураамж + түрээс + алданги (US-12, US-13). Алдангийг `suh/late_fee.py` тооцно: хоногт 0.5%-иас ихгүй, нийт 50%-иас хэтрэхгүй (Иргэний хуулийн 232.4, 232.6).
- `amount_due(invoice_id, repo, today, daily_rate)`: нэхэмжлэхийг өгөгдлийн сангаас (`repo`) уншиж, өнөөдрийн байдлаар төлөх дүнг гаргана.

## 3. Тестүүд (`tests/test_billing.py`)

Тест бүр `# Arrange`, `# Act`, `# Assert` гэсэн гурван хэсэгтэй.

| № | Тест | Төрөл | Шалгах зүйл |
|---|---|---|---|
| 1 | `test_total_on_time_is_fee_plus_rent` | Хэвийн | Хугацаандаа бол 45,000 + 60,000 = 105,000₮ |
| 2 | `test_total_with_seven_days_late_fee` | Хэвийн | 7 хоног хэтэрвэл 100,000₮ + 3,500₮ алданги |
| 3 | `test_zero_fee_and_rent_gives_zero` | Хилийн | Хоосон (0) дүн 30 хоног хэтэрсэн ч 0 |
| 4 | `test_negative_amount_is_rejected` | Хилийн | Сөрөг хураамж эсвэл түрээс `ValueError` |
| 5 | `test_very_late_fee_is_capped_at_half` | Хилийн | Маш том дүн, 10 жил хэтэрсэн ч алданги 50% |
| 6 | `test_amount_due_reads_invoice_from_repository` | Mock | Өгөгдлийн сангийн оронд `unittest.mock.Mock`, `get_invoice(7)` нэг удаа дуудагдсан |

Mock-ийн давуу тал: жинхэнэ өгөгдлийн сан, сүлжээ шаардлагагүй тул тест хурдан, тогтвортой ажиллана, зөвхөн тооцооны логикийг шалгана.

## 4. Локал ажиллуулсан үр дүн

```
$ pytest -v
...
tests/test_billing.py::test_amount_due_reads_invoice_from_repository PASSED
...
============================== 24 passed in 0.03s ==============================
```

Нийт 24 тест (дарааллын 8, алдангийн 9, нэхэмжлэхийн 7) амжилттай.

## 5. CI-д нэгтгэх

Лаб 7-ийн `.github/workflows/ci.yml` push, pull request бүрт `pytest -v` ажиллуулдаг тул шинэ тест нэмэлт тохиргоогүйгээр CI-д орно.

## 6. Санаатайгаар унагаах

`demo/lab10-ulaan` branch-д `invoice_total()`-д алдангийг нэмэхээ мартсан алдаа оруулж push хийв. CI дээр 3 тест (7 хоногийн алданги, 50%-ийн хязгаар, mock-той amount_due) унаж, Pull Request улаан болсон. Энэ branch-ийг merge хийхгүй.
