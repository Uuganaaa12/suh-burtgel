# Лабораторийн ажил №2 — User Story ба Backlog

## 1. Төслийн зорилго, хамрах хүрээ

**Бид ямар асуудлыг шийдэх гэж байна вэ?** СӨХ оршин суугч, машин, зогсоолын мэдээллээ тусад нь хөтөлдөг тул зогсоолын маргаан гарч, харуул гадны машиныг ялгаж чаддаггүй.

**Хэнд туслах вэ?** Оршин суугч, СӨХ-ийн гүйцэтгэх захирал, нягтлан бодогч, харуул.

**Үндсэн функцууд:** оршин суугчийн бүртгэл, машины бүртгэл, зогсоолын хуваарилалт, хаалганы хяналт, сарын төлбөр.

## 2. User Story-ийн формат

`As a [хэрэглэгчийн төрөл], I want [зорилго], so that [шалтгаан].`

## 3. User Story-ууд

Дипломын ажилд тодорхойлсон юз кейзүүд дээр тулгуурлан бичив. Юз кейз нь системийн үйлдлийг, User Story нь хэрэглэгчийн хүсэлтийг илэрхийлдэг тул хоёрыг зэрэгцүүлэн харуулав.

**US-01** (UC — нэвтрэлт)  
As a resident, I want to log in with my phone number and password, so that only I can see my apartment data.  
*Оршин суугч утасны дугаар, нууц үгээрээ нэвтэрч, зөвхөн өөрийн сууцны мэдээллийг харна.*

**US-02** (UC-02)  
As a manager, I want to register a resident and link them to an apartment, so that I know who lives in each unit.  
*Гүйцэтгэх захирал оршин суугчийг сууцтай нь холбож бүртгэнэ.*

**US-03** (UC-03)  
As an owner, I want to register my tenant with a contract period, so that the tenant can use the system while renting.  
*Сууц өмчлөгч түрээслэгчээ гэрээний хугацаатай нь бүртгүүлнэ.*

**US-04** (UC-04)  
As a resident, I want to register my car with its plate number, so that the guard can recognise it at the gate.  
*Оршин суугч машинаа улсын дугаараар нь бүртгүүлнэ.*

**US-05** (UC-06)  
As a manager, I want to approve new car registrations, so that only checked cars get access.  
*Гүйцэтгэх захирал шинэ машины бүртгэлийг баталгаажуулна.*

**US-06** (UC-07)  
As a resident, I want to request a parking space, so that I can park my car in the yard.  
*Оршин суугч зогсоолын хүсэлт илгээнэ.*

**US-07** (UC-08)  
As a resident, I want to see my position in the parking waiting list, so that I know when my turn comes.  
*Оршин суугч хүлээлгийн жагсаалтад хэддүгээрт байгаагаа харна.*

**US-08** (UC-09)  
As a manager, I want to assign a parking space to an apartment, so that spaces are shared in order of request.  
*Гүйцэтгэх захирал зогсоолыг сууцад хуваарилна.*

**US-09** (UC-10)  
As a resident, I want to book a guest parking space for a chosen time, so that my visitor can park.  
*Оршин суугч зочиндоо тодорхой цагт зогсоол захиална.*

**US-10** (UC-11)  
As a resident, I want to get a one-time access code for my guest, so that the guard can let the guest in.  
*Оршин суугч зочиндоо нэг удаагийн нэвтрэх код авна.*

**US-11** (UC-12)  
As a guard, I want to check a car by its plate number, so that I can tell residents from strangers.  
*Харуул улсын дугаараар машиныг шалгана.*

**US-12** (UC-14)  
As a guard, I want to record a parking violation with a photo, so that the manager can take action.  
*Харуул зөрчлийг зурагтай нь бүртгэнэ.*

**US-13** (UC-15)  
As an accountant, I want to generate monthly invoices for all apartments, so that residents know what to pay.  
*Нягтлан бодогч сар бүрийн нэхэмжлэхийг үүсгэнэ.*

**US-14** (UC-16)  
As a resident, I want to pay my invoice with QPay, so that I do not have to go to the office.  
*Оршин суугч нэхэмжлэхээ QPay-ээр төлнө.*

**US-15** (UC-18)  
As a manager, I want to publish an announcement to residents, so that everyone gets the same information.  
*Гүйцэтгэх захирал оршин суугчдад зарлал нийтэлнэ.*

## 4. INVEST шалгалт

| Зарчим | Шалгасан байдал |
|---|---|
| Independent | Story бүр өөр story дуусахыг хүлээхгүйгээр хийгдэнэ. US-05 нь US-04-өөс хамаарах тул Backlog дээр дараалуулан байрлуулав. |
| Negotiable | Story бүр юу хийхийг зааж байгаа ч хэрхэн хийхийг заагаагүй. Дэлгэцийн зохиомжийг Sprint-ийн үеэр хэлэлцэнэ. |
| Valuable | Story бүр оршин суугч, захирал, харуул, нягтлангийн аль нэгэнд бодит үр өгөөжтэй. |
| Estimable | Story бүрийг Лаб 3-д Story Point-оор үнэлэв. Хэт том нь байсангүй. |
| Small | «Зогсоол хуваарилах», «Хүлээлгийн жагсаалтаа харах» хоёрыг тусад нь салгав. Эхэндээ нэг story байсныг INVEST-ийн дагуу хоёр болгож задлав. |
| Testable | Story бүрийг «хийгдсэн эсэх»-ийг нүдээр шалгана. Жишээ нь US-11-д бүртгэлтэй, бүртгэлгүй хоёр дугаар оруулж дүнг харна. |

## 5. Бүтээгдэхүүний Backlog

Backlog-ийг [backlog.csv](../backlog.csv) файлд хөтөлж, GitHub Projects дээр `To do / In Progress / Done` баганатайгаар үүсгэв.

| ID | User Story | Priority | Notes |
|---|---|---|---|
| US-01 | As a resident, I want to log in with my phone number and password, so that only I can see my apartment data. | High | Must have |
| US-02 | As a manager, I want to register a resident and link them to an apartment, so that I know who lives in each unit. | High | Must have |
| US-03 | As an owner, I want to register my tenant with a contract period, so that the tenant can use the system while renting. | Medium |  |
| US-04 | As a resident, I want to register my car with its plate number, so that the guard can recognise it at the gate. | High | Must have |
| US-05 | As a manager, I want to approve new car registrations, so that only checked cars get access. | High | Must have |
| US-06 | As a resident, I want to request a parking space, so that I can park my car in the yard. | High | Must have |
| US-07 | As a resident, I want to see my position in the parking waiting list, so that I know when my turn comes. | Medium |  |
| US-08 | As a manager, I want to assign a parking space to an apartment, so that spaces are shared in order of request. | High | Must have |
| US-09 | As a resident, I want to book a guest parking space for a chosen time, so that my visitor can park. | Medium |  |
| US-10 | As a resident, I want to get a one-time access code for my guest, so that the guard can let the guest in. | Medium |  |
| US-11 | As a guard, I want to check a car by its plate number, so that I can tell residents from strangers. | High | Must have |
| US-12 | As a guard, I want to record a parking violation with a photo, so that the manager can take action. | Low |  |
| US-13 | As an accountant, I want to generate monthly invoices for all apartments, so that residents know what to pay. | High | Must have |
| US-14 | As a resident, I want to pay my invoice with QPay, so that I do not have to go to the office. | High | Must have |
| US-15 | As a manager, I want to publish an announcement to residents, so that everyone gets the same information. | Low |  |

## Гүйцэтгэлийн шалгуур

- [x] Багийн хамт төслийн зорилго, үндсэн функцуудыг тодорхойлсон
- [x] User Story-ийн зөв форматыг ашигласан
- [x] INVEST зарчмыг шалгасан
- [x] 15 ширхэг User Story бичсэн
- [ ] Backlog-ийг GitHub Projects дээр үүсгэсэн
- [x] User Story-ууд тодорхой, туршигдахуйц, үнэ цэнэтэй
