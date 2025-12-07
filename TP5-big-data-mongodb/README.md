# BIG_DATA_TP5-mongodb
```js
#i use pop os linux
#تحديث النظام
sudo apt update && sudo apt upgrade -y
#استيراد المفتاح GPG
curl -fsSL https://pgp.mongodb.com/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
#إضافة المستودع
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
#تحديث الحزم
sudo apt update
#تثبيت MongoDB
sudo apt install -y mongodb-org
# تشغيل MongoDB
sudo systemctl start mongod
#فتح Mongo Shell
mongosh
# تنفيذ TP5
test> use info
switched to db info
info> db.produits.insertOne({
...     nom: "Macbook Pro",
...     fabriquant: "Apple",
...     prix: 11435.99,
...     options: [
...         "Intel Core i5",
...         "Retina Display",
...         "Long life battery"
...     ]
... })
{
  acknowledged: true,
  insertedId: ObjectId('692430ff5a0e6418199dc29d')
}
info> db.produits.insertOne({
...     nom: "Macbook Air",
...     fabriquant: "Apple",
...     prix: 125794.73,
...     ultrabook: true,
...     options: [
...         "Intel Core i7",
...         "SSD",
...         "Long life battery"
...     ]
... })
{
  acknowledged: true,
  insertedId: ObjectId('6924310a5a0e6418199dc29e')
}
info> db.produits.insertOne({
...     nom: "Thinkpad X230",
...     fabriquant: "Lenovo",
...     prix: 114358.74,
...     ultrabook: true,
...     options: [
...         "Intel Core i5",
...         "SSD",
...         "Long life battery"
...     ]
... })
{
  acknowledged: true,
  insertedId: ObjectId('692431225a0e6418199dc29f')
}
info> db.produits.find()
[
  {
    _id: ObjectId('692430ff5a0e6418199dc29d'),
    nom: 'Macbook Pro',
    fabriquant: 'Apple',
    prix: 11435.99,
    options: [ 'Intel Core i5', 'Retina Display', 'Long life battery' ]
  },
  {
    _id: ObjectId('6924310a5a0e6418199dc29e'),
    nom: 'Macbook Air',
    fabriquant: 'Apple',
    prix: 125794.73,
    ultrabook: true,
    options: [ 'Intel Core i7', 'SSD', 'Long life battery' ]
  },
  {
    _id: ObjectId('692431225a0e6418199dc29f'),
    nom: 'Thinkpad X230',
    fabriquant: 'Lenovo',
    prix: 114358.74,
    ultrabook: true,
    options: [ 'Intel Core i5', 'SSD', 'Long life battery' ]
  }
]
info> db.produits.findOne()
{
  _id: ObjectId('692430ff5a0e6418199dc29d'),
  nom: 'Macbook Pro',
  fabriquant: 'Apple',
  prix: 11435.99,
  options: [ 'Intel Core i5', 'Retina Display', 'Long life battery' ]
}
info> db.produits.findOne({ nom: "Thinkpad X230" })
{
  _id: ObjectId('692431225a0e6418199dc29f'),
  nom: 'Thinkpad X230',
  fabriquant: 'Lenovo',
  prix: 114358.74,
  ultrabook: true,
  options: [ 'Intel Core i5', 'SSD', 'Long life battery' ]
}
info> db.produits.findOne({ _id: ObjectId("692431225a0e6418199dc29f") })
{
  _id: ObjectId('692431225a0e6418199dc29f'),
  nom: 'Thinkpad X230',
  fabriquant: 'Lenovo',
  prix: 114358.74,
  ultrabook: true,
  options: [ 'Intel Core i5', 'SSD', 'Long life battery' ]
}
info> db.produits.find({ prix: { $gt: 13723 } })
[
  {
    _id: ObjectId('6924310a5a0e6418199dc29e'),
    nom: 'Macbook Air',
    fabriquant: 'Apple',
    prix: 125794.73,
    ultrabook: true,
    options: [ 'Intel Core i7', 'SSD', 'Long life battery' ]
  },
  {
    _id: ObjectId('692431225a0e6418199dc29f'),
    nom: 'Thinkpad X230',
    fabriquant: 'Lenovo',
    prix: 114358.74,
    ultrabook: true,
    options: [ 'Intel Core i5', 'SSD', 'Long life battery' ]
  }
]
info> db.produits.findOne({ ultrabook: true })
{
  _id: ObjectId('6924310a5a0e6418199dc29e'),
  nom: 'Macbook Air',
  fabriquant: 'Apple',
  prix: 125794.73,
  ultrabook: true,
  options: [ 'Intel Core i7', 'SSD', 'Long life battery' ]
}
info> db.produits.findOne({ nom: /Macbook/ })
{
  _id: ObjectId('692430ff5a0e6418199dc29d'),
  nom: 'Macbook Pro',
  fabriquant: 'Apple',
  prix: 11435.99,
  options: [ 'Intel Core i5', 'Retina Display', 'Long life battery' ]
}
info> db.produits.find({ nom: /^Macbook/ })
[
  {
    _id: ObjectId('692430ff5a0e6418199dc29d'),
    nom: 'Macbook Pro',
    fabriquant: 'Apple',
    prix: 11435.99,
    options: [ 'Intel Core i5', 'Retina Display', 'Long life battery' ]
  },
  {
    _id: ObjectId('6924310a5a0e6418199dc29e'),
    nom: 'Macbook Air',
    fabriquant: 'Apple',
    prix: 125794.73,
    ultrabook: true,
    options: [ 'Intel Core i7', 'SSD', 'Long life battery' ]
  }
]
info> db.produits.deleteMany({ fabriquant: "Apple" })
{ acknowledged: true, deletedCount: 2 }
info> db.produits.find()
[
  {
    _id: ObjectId('692431225a0e6418199dc29f'),
    nom: 'Thinkpad X230',
    fabriquant: 'Lenovo',
    prix: 114358.74,
    ultrabook: true,
    options: [ 'Intel Core i5', 'SSD', 'Long life battery' ]
  }
]
info> db.produits.deleteOne({ _id: ObjectId("692431225a0e6418199dc29f") })
{ acknowledged: true, deletedCount: 1 }
info> db.produits.find()

info> exit
```js
