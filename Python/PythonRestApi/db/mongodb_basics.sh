db
db.version()

use my_db

show dbs
db.movie.insertOne({"name": "Die Hard"})
db.dropDatabase()

// Create Collection
use test
db.createCollection("my_collection")
show collections

db.createCollection("my_col", {capped: true, size: 3, max: 3})
show collections

db.magical_collection.insertOne({"Name": "Magical collection created"})
show collections

// Delete database
use my_db
db.createCollection("delete")
show collections
db.dropDatabase()
show collections

// Insert into documents into collection
use test
show collections
db.createCollection("my_collection")
db.my_collection.insertOne({Username: "Adam", Password: "123"})
db.my_collection.insertMany([
    {Username: "Bengt", Password: "234"},
    {Username: "Cecar", Password: "345"},
    {Username: "David", Password: "456"},
])
db.my_collection.find()

// Query documents
db.my_collection.find()
db.my_collection.find().pretty()

db.my_collection.findOne({Username: "Bengt"})

// Filters
// Equality
db.my_collection.find({Password: "234"})
// Less than
db.my_collection.find({Password: {$lt: "345"}})
// Less than Equals
db.my_collection.find({Password: {$lte: "345"}})
// Greater Than
db.my_collection.find({Password: {$gt: "234"}})
// Greater Than Equals
db.my_collection.find({Password: {$gte: "234"}})
// Not Equals
db.my_collection.find({Password: {$ne: "234"}})

// AND
db.my_collection.find({$and: [{Username: {$ne: "Adam"}}, {Password: {$ne: "345"}}]})

// OR
db.my_collection.find({$or: [{Username: "Adam"}, {Password: "345"}]})


// UPDATE - Updates specific field
db.my_collection.find().count()
db.my_collection.insertOne({Username: "Lars", Password: "123"})
db.my_collection.find().count()

selection_criteria = {Username: "Lars"}
updated_data = {Password: "321"}

db.my_collection.updateOne(selection_criteria, {$set: updated_data})
db.my_collection.find(selection_criteria)

db.my_collection.deleteOne(selection_criteria)
db.my_collection.find().count()

// SAVE - Scraps document and replaces with new
db.my_collection.find().count()
db.my_collection.insertOne({Username: "Lars", Password: "123"})
db.my_collection.find().count()

db.my_collection.find()
db.my_collection.replaceOne(selection_criteria, updated_data)
db.my_collection.find()
db.my_collection.deleteOne(updated_data)
db.my_collection.find()

// Projection
db.my_collection.find({}, {Username: 1})
db.my_collection.find({}, {Password: 1})
db.my_collection.find({}, {Username: 1, _id : 0})
db.my_collection.find({}, {Password: 1, _id : 0})

// Limit
db.my_collection.find({}, {Username: 1, _id : 0}).limit(2)

// Sort
db.my_collection.find({}, {Username: 1, _id : 0}).sort({Username: 1})
db.my_collection.find({}, {Username: 1, _id : 0}).sort({Username: -1})
db.my_collection.find({}, {Username: 1, _id : 0}).limit(2).sort({Username: -1})

