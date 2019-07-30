## M - Service Area



### Deployed Project / Features

The project is deployed on AWS server.

####  Main Page (Provider)
_http://ec2-13-233-57-77.ap-south-1.compute.amazonaws.com/_

REST (CRUD) APIs for Providers, Languages, Currencies
Seeded publicly data available for Language + Currencies

#### Admin Portal
_http://ec2-13-233-57-77.ap-south-1.compute.amazonaws.com/admin/_

**User Credentials:**

_Username_: monk | 
_Password_: knom


It has CRUD operations available for Service Areas, Currencies, Languages, Providers

#### Service Areas API

http://ec2-13-233-57-77.ap-south-1.compute.amazonaws.com/service-areas/

The feature allows to add Service Area along with Name, Price and a Provider
The above GET retrieves a UI to enter the various details for addition.
POST request is made for final creation of the Service Area.

#### Services Area Query

http://ec2-13-233-57-77.ap-south-1.compute.amazonaws.com/service-areas/query?lon={longitude}&lat={latitude}

This GET API is used to query and fetch all the available services area which contain the requested latitude
and longitude and empty array in case of empty scenario.

### Issues Encountered

- Amazon account was new and they sometime restrict creation of instances readily, it can take upto 24 hours sometimes. Wasted a lot of time.
- Was creating separate view

### Left Out Portal / Couldn't Complete

- Testing (No Test Cases). Could only carry out Minor Unit Testing at my end.
- Validation with any Linting tool for PEP8
- Proper Comments (Missing docstrings)
- Couldn't setup env variables in time and all the settings are exposed.

Was short on time and couldn't complete above.


