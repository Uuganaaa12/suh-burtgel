# Лабораторийн ажил №7 — GitHub Actions ашиглан CI Pipeline байгуулах

Хичээл: Программ хангамж хөгжүүлэлтийн процесс (7-р долоо хоног)\
Төсөл: СӨХ-ийн сууц, машин, зогсоолын бүртгэлийн систем\
Баг: Д.Ууганбаяр (Product Owner), Ц.Номунзаяа (Scrum Master)\
Repository: <https://github.com/Uuganaaa12/suh-burtgel>

## 1. Зорилго

- GitHub Actions workflow файлыг бие даан бичих.
- push, Pull Request бүрт тестийг автоматаар ажиллуулах.
- Pipeline-ийн амжилттай, амжилтгүй үр дүнг уншиж тайлбарлах.

## 2. Тестлэх код

Төслийн гол дүрэм болох зогсоолын хүлээлгийн дарааллыг Python-оор бичив (`suh/queue.py`). Хүсэлтүүд зөвхөн ирсэн цагаараа эрэмбэлэгдэнэ. Өмнө зогсоол түрээсэлсэн эсэх эрэмбэд нөлөөлөхгүй (ФШ-12). `position()` нь хүсэлтийн дарааллын дугаарыг буцаана (US-07).

`tests/test_queue.py` 8 тесттэй: огноогоор эрэмбэлэх, нэг өдрийн хүсэлтийг цагаар эрэмбэлэх, хоосон жагсаалт, оролтын жагсаалт өөрчлөгдөхгүй байх, дарааллын дугаар, байхгүй хүсэлт.

## 3. Workflow

`.github/workflows/ci.yml`:

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install
        run: pip install -r requirements.txt

      - name: Test
        run: pytest -v
```

| Алхам | Юу хийх |
|---|---|
| Checkout | Repository-ийн кодыг runner руу татна |
| Setup Python | Python 3.12 суулгана |
| Install | `requirements.txt`-ийн хамаарлыг (pytest) суулгана |
| Test | `pytest -v` ажиллуулна. Тест унавал алхам, pipeline хоёулаа улаан болно |

Trigger нь `push` ба `pull_request` тул branch руу push хийх, PR нээх бүрт pipeline автоматаар эхэлнэ.

## 4. Амжилттай ба амжилтгүй ажиллагаа

- `feature/ci` branch — бүх тест тэнцэж pipeline ногоон болно.
- `demo/ci-ulaan` branch — `test_ordered_by_request_date` тестийн хүлээгдэх утгыг санаатайгаар `["R1", "R2", "R3", "R4"]` болгосон. Зөв эрэмбэ нь `R4, R1, R3, R2` тул Test алхам `AssertionError`-оор унаж pipeline улаан болно. Энэ branch-ийг `main` руу merge хийхгүй.
