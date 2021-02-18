// Denna fil går att ladda in i Mongo med: mongo < create_db.js
// Den skapar upp hela exempeldatabasen och kör de frågor som
// efterfrågas i inlämningsuppgiften. Visar även CRUD-exempel.

// Skapa/använd databasen
use kt_inlamning2;

// Rensa databasen på all data
db.dropDatabase()

// Ladda in all data om bankkontona
db.bank_accounts.insertMany(JSON.parse(cat("bank_accounts.json")));

// Skapa en collection med adresser
db.locations.insertMany(
    [
        { country: "SE", address: "Vimmerbygatan 20" },
        { country: "US", address: "Asteroid road 5" },
        { country: "US", address: "Comet road 41" },
        { country: "SE", address: "Brunnsgatan 7" },

    ]
)

// Lägg in nya konton 
db.bank_accounts.insert({ id: "1001", first_name: "Corbin", last_name: "Hauck", holding: 234567 })
db.bank_accounts.insert({ id: "1002", first_name: "Vanya", last_name: "Worsell", holding: 3234567 })
db.bank_accounts.insert({ id: "1003", first_name: "Eldon", last_name: "McCartan", holding: 6234567 })
db.bank_accounts.insert({ id: "1004", first_name: "Ingunna", last_name: "Castellucci", holding: 7234567 })

// Knyt de nya kontona med adresser.
// Här visar jag 2 varianter, en med DBRef och en med embedded document
var ref = db.locations.findOne({ address: "Brunnsgatan 7" })
db.bank_accounts.updateOne({ id: "1001" }, { $set: { location: { country: ref.country, address: ref.address } } })

var ref = db.locations.findOne({ address: "Asteroid road 5" })
db.bank_accounts.updateOne({ id: "1002" }, { $set: { location: { country: ref.country, address: ref.address } } })

var ref = db.locations.findOne({ address: "Vimmerbygatan 20" }, { _id: 1 })
db.bank_accounts.updateOne({ id: "1003" }, { $set: { location: { $ref: "locations", $id: ref._id } } })

var ref = db.locations.findOne({ address: "Comet road 41" }, { _id: 1 })
db.bank_accounts.updateOne({ id: "1004" }, { $set: { location: { $ref: "locations", $id: ref._id } } })




print("\n\n\n\n")
var div="\n===============================================================\n"

// En query för att plocka ut de adresser där country="SE"
// Här använder jag $lookup för att hämta informationen om DBRef.
// Denna info sparas i en ny key, "location1". Detta för att inte skriva över "location".
// Sedan gör jag en sökning efter country i "location" och "location1".
print(div + "En query för att plocka ut de adresser med country=SE" + div)
db.bank_accounts.aggregate(
    {
        $lookup: {
            from: "locations",
            localField: "location.$id",
            foreignField: "_id",
            as: "location1"
        }
    },
    {
        $match: {
             $or: [
                {"location.country": "SE"},
                {"location1.country": "SE"}
            ]
        }
    }
).pretty()


// Visar CRUD
print(div + "Visar CRUD")
print("CREATE: db.devops.insert({first_name: 'Kent', last_name: 'Thureson'})" + div)
db.devops.insert({first_name: 'Kent', last_name: 'Thureson'})
db.devops.find()

print(div + "READ: db.devops.find({first_name: 'Kent'})" + div)
db.devops.find({first_name: 'Kent'})

print(div + "UPDATE: db.devops.update({first_name: 'Kent'}, {$set: {last_name: 'Thureson updated'}})" + div)
db.devops.update({first_name: 'Kent'}, {$set: {last_name: "Thureson updated"}})
db.devops.find()

print(div + "DELETE: db.devops.remove({first_name: 'Kent'})" + div)
db.devops.remove({first_name: 'Kent'})
db.devops.find()
