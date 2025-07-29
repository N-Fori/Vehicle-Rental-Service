# Vehicle Rental Service

A simple vehicle rental system in Python that manages cars and motorcycles, rental transactions, and vehicle availability.

## Main Classes

### `Vehicle`
Base vehicle class that contains basic vehicle information (VIN, make, model, daily rate), as well as methods to start and end rentals and track availability status.

### `Car` (inherits from `Vehicle`)
Car-specific class that includes passenger capacity.

### `Motorcycle` (inherits from `Vehicle`)
Motorcycle-specific class that includes engine size (cc).

### `Rental`
Represents a rental transaction, storing rental ID, the vehicle rented, customer name, rental duration, and rental status. Also calculates rental cost.

### `RentalAgency`
Represents the rental agency that manages vehicles and rentals. Supports adding vehicles, renting them out, returning rentals, and querying available vehicles.

## Usage

- Add new vehicles to the rental agency.
- Rent vehicles to customers for a specified number of days.
- End rentals and return vehicles.
- Query available vehicles for rent.

---

## Author

**Nándor Forgó**  
Email: nfori.coding@gmail.com  
GitHub: [N-Fori](https://github.com/N-Fori)
