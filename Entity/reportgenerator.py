from tabulate import tabulate
class ReportGenerator:
    def __init__(self, reserv_service, vehicle_service):
        self.reserv_service = reserv_service
        self.vehicle_service = vehicle_service
    
    def generate_reservation_report(self):
        reservations, headers = self.reserv_service.GetReservations()
        
        if reservations:
            print(tabulate(reservations,headers=headers,tablefmt="psql"))
            total_revenue = sum(reservation[5] for reservation in reservations)
            print(f"Total Revenue: {total_revenue}")
        else:
            print("No reservations found")
    
    def generate_vehicle_report(self):
        vehicles, headers = self.vehicle_service.GetAllVehicles()
        
        if vehicles:
            print(tabulate(vehicles,headers=headers, tablefmt="psql"))
        else:
            print("No vehicles found")
