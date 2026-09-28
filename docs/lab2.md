# Лабораторийн ажил №2 — Хэрэглэгчийн хэрэгцээг ойлгох ба User Story бичих

## 1. Төслийн зорилго, хамрах хүрээ

Багаар хэлэлцээд дараах гурван асуултад хариулав.

**Бид ямар асуудлыг шийдэх гэж байна вэ?**
СӨХ сууц, машин, зогсоолын мэдээллээ дэвтэр, Excel дээр тусад нь хөтөлдөг. Машины зогсоол нь хуулиар сууц өмчлөгчдийн дундын өмчлөл боловч хэнд, ямар журмаар олгосныг хянах бичиг баримт байдаггүй. Үүнээс зогсоолын маргаан үүсдэг.

**Бидний бүтээх зүйл хэнд туслах вэ?**
Оршин суугч ба СӨХ-ийн менежерт. Оршин суугч гар утсаараа машинаа бүртгүүлж, зогсоол хүсэж, дараалалдаа хяналт тавьж, нэхэмжлэхээ харна. Төлбөрөө өөрийн банкны аппаар сууцны кодоор төлнө. Менежер вэбээр бүртгэл хөтөлж, зогсоол олгож, нэхэмжлэх үүсгэж, тайлан гаргана.

**Үндсэн функцууд:**

1. Сууц, зогсоолын бүртгэл.
2. Машины бүртгэл, баталгаажуулалт.
3. Зогсоолын түрээсийн хүсэлт ба ил тод хүлээлгийн жагсаалт.
4. Зогсоол олгох, олголтын шийдвэрийг шалтгаантай нь хадгалах.
5. Сарын нэхэмжлэх, банкны аппаар төлсөн төлбөрийн бүртгэл, тайлан.

Гурван төрлийн хэрэглэгч: **оршин суугч**, **СӨХ-ийн менежер**, гадаад систем болох **банкны апп**.

## 2. User Story-ийн формат

`As a [хэрэглэгчийн төрөл], I want [зорилго], so that [шалтгаан].`

Монголчлон: [хэрэглэгчийн төрөл] нь [юу хийхийг] хүсэж байна, [ямар шалтгаанаар].

Story бүрийг хэрэглэгчийн үүднээс бичив. Техникийн шийдэл, өгөгдлийн сангийн бүтцийг story-д оруулаагүй.

## 3. User Story-ууд

15 story бичив. Хаалтанд дипломын ажлын юзкейсийн дугаарыг зааж, хоёр баримтыг хооронд нь уялдуулав.

**US-01** (бүх юзкейсийн өмнөх нөхцөл)
As a resident, I want to log in with my Gmail (Google) account, so that only I can see my own apartment data.
*Оршин суугч Gmail бүртгэлээрээ нэвтэрч, зөвхөн өөрийн сууцны мэдээллийг харна.*

**US-02** (UC-01)
As a manager, I want to register an apartment together with its resident, so that every unit has one responsible contact.
*Менежер сууцыг оршин суугчийнх нь хамт бүртгэнэ.*

**US-03** (UC-02)
As a manager, I want to register each parking space with its ownership type, so that only common-property spaces go into the queue.
*Менежер зогсоол бүрийг өмчлөлийн төрөлтэй нь бүртгэж, зөвхөн дундын өмчлөлийнхийг дараалалд оруулна.*

**US-04** (UC-03)
As a resident, I want to register my car with its plate number, so that it can be checked and approved.
*Оршин суугч машинаа улсын дугаараар бүртгүүлнэ.*

**US-05** (UC-04)
As a manager, I want to approve or reject a registered car with a reason, so that only checked cars can rent a space.
*Менежер бүртгүүлсэн машиныг батална эсвэл шалтгаан бичиж татгалзана.*

**US-06** (UC-05)
As a resident, I want to request a parking space for a chosen period, so that I can park in the yard of my building.
*Оршин суугч сонгосон хугацаагаар зогсоолын түрээсийн хүсэлт илгээнэ.*

**US-07** (UC-05)
As a resident, I want to see my position in the waiting list, so that I know when my turn comes.
*Оршин суугч хүлээлгийн жагсаалтад хэддүгээрт байгаагаа харна.*

**US-08** (UC-05)
As a resident, I want to see the whole waiting list, so that I can check the order is kept.
*Оршин суугч бүх хүлээлгийн жагсаалтыг хараад дарааллыг шалгана.*

**US-09** (UC-05, UC-06)
As a resident with no parking space, I want first-car requests to come before additional-car requests, so that every apartment gets one space before anyone gets two.
*Зогсоолгүй оршин суугчийн хувьд нэг дэх машины хүсэлт нэмэлт машины хүсэлтээс түрүүлнэ.*

**US-10** (UC-06)
As a manager, I want to allocate a free space to the first request in the queue, so that the lease starts on the agreed date.
*Менежер сул зогсоолыг дарааллын эхний хүсэлтэд олгоно.*

**US-11** (UC-06)
As a resident, I want every out-of-order allocation to be recorded with its reason, manager and date, so that the decision can be checked later.
*Дарааллаас гадуур олгосон зогсоол бүрийг шалтгаан, шийдвэр гаргасан менежер, огнооных нь хамт бүртгэж, бүх оршин суугчдад харуулна.*

**US-12** (UC-07)
As a manager, I want the system to create monthly invoices for every apartment, so that residents know what to pay.
*Менежер сар бүр сууц тус бүрд нэхэмжлэх үүсгэнэ.*

**US-13** (UC-08)
As a resident, I want to see my invoices, including any late fee, and my payment history, so that I know how much to pay in my bank app.
*Оршин суугч сууцныхаа нэхэмжлэхийн төлөв, задаргаа, төлбөрийн түүх, банкны аппад оруулах сууцны кодыг харна. Хугацаа хэтэрсэн нэхэмжлэхэд систем алданги бодож нэмнэ.*

**US-14** (UC-10)
As a manager, I want payments that residents make in their bank app to be recorded automatically, so that I do not have to match payments by hand.
*Систем төлөгдөөгүй нэхэмжлэхийн дүнг сууцны кодоор банкны аппад харуулж, банкны апп төлбөр төлөгдсөнийг мэдэгдэхэд нэхэмжлэхийг төлөгдсөн болгон баримт үүсгэнэ.*

**US-15** (UC-09)
As a manager, I want to export a report for a chosen period to Excel, so that I can present it at the owners' meeting.
*Менежер сонгосон хугацааны тайланг Excel файлаар татна.*

## 4. INVEST зарчмаар шалгасан байдал

| ID | I | N | V | E | S | T | Тэмдэглэл |
|---|---|---|---|---|---|---|---|
| US-01 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | Нэвтрэлт нь бусад story-гийн өмнөх нөхцөл ч тусдаа хүргэгдэнэ |
| US-02 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | |
| US-03 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | |
| US-04 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | |
| US-05 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | |
| US-06 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | US-10-аас хамаарахгүй, хүсэлт дангаараа хадгалагдана |
| US-07 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | Хамгийн жижиг story, үнэлгээний суурь болов |
| US-08 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | |
| US-09 | — | ✔ | ✔ | ✔ | ✔ | ✔ | US-06-гийн эрэмбийн дүрэм тул бүрэн бие даасан биш |
| US-10 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | |
| US-11 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | |
| US-12 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | |
| US-13 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | |
| US-14 | — | ✔ | ✔ | ✔ | ✔ | ✔ | Банкны аппын холболтоос хамаарна |
| US-15 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | |

Шалгах явцад гурван story-г засав.

1. «Зогсоолын систем ажиллуулах» гэсэн нэг том story нь Small шалгуурыг хангахгүй байсан тул US-06, US-07, US-10 гурав болгон задлав.
2. «Систем ил тод байх» гэсэн story нь Estimable биш байв. Хэмжиж болохоор US-08, US-11 хоёр болгон тодорхой бичив.
3. «Систем банкны аппын API-тай холбогдоно» гэсэн техникийн story нь Valuable шалгуурыг хангахгүй байсан тул менежерийн үүднээс US-14 болгон дахин бичив.

## 5. Бүтээгдэхүүний Backlog

Backlog-ийг repository дотор [`backlog.csv`](../backlog.csv), мөн [`backlog.xlsx`](../backlog.xlsx) файлд хөтөлнө. Excel файлд «Product Backlog», «Sprint 1 Backlog» гэсэн хоёр хуудас бий. Баганууд:

| Багана | Утга |
|---|---|
| ID | US-01 … US-15 |
| User Story | Стандарт форматаар |
| Монгол тайлбар | Багийн уулзалтад ашиглах |
| Юзкейс | Дипломын ажлын юзкейсийн дугаар |
| Priority | High / Medium / Low |
| Story Point | Лаб 3-д тогтоов |
| Status | To do / In Progress / Done |
| Notes | MoSCoW ангилал |

Эрэмбийг Product Owner тогтоов. Бүртгэл, зогсоол олголт, төлбөрийн story-нууд High, ил тод байдлын болон тайлангийн story-нууд Medium байна.

## 6. Дүгнэлт

Төслийн зорилго, хэрэглэгчдийг тодорхойлж, 15 User Story бичиж, INVEST зарчмаар шалгаж, гурвыг нь засав. Backlog нь repository дотор хадгалагдаж байгаа тул хоёр гишүүн хоёулаа өөрчлөлт оруулна. Энэ backlog дээр Лаб 3-ын Story Point, Sprint 1-ийн төлөвлөгөө тулгуурлана.

## Биелэлтийн шалгуур

- [x] Багийн хамт төслийн зорилго, үндсэн функцуудыг тодорхойлсон
- [x] User Story-ийн зөв форматыг ашигласан
- [x] INVEST зарчмаар шалгаж, шаардлагатай story-г засварласан
- [x] 15 ширхэг User Story бичсэн
- [x] Бүтээгдэхүүний Backlog-ийг үүсгэсэн (`backlog.csv`, `backlog.xlsx`)
- [x] User Story-ууд тодорхой, туршигдах, үнэ цэнэтэй байна
