from tabulate import tabulate
import csv
class ReportGenerator:
    def __init__(self, reserv_service, vehicle_service):
        self.reserv_service = reserv_service
        self.vehicle_service = vehicle_service
    
    def generate_reservation_report(self):
        reservations, headers = self.reserv_service.GetReservationReport()
        
        if reservations:
            print(tabulate(reservations,headers=headers,tablefmt="psql"))
            total_revenue = sum(reservation[8] for reservation in reservations)
            print(f"Total Revenue: {total_revenue}")
            with open("ReservationReport.csv","w",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(reservations)
        else:
            print("No reservations found")
    
    def generate_vehicle_report(self):
        vehicles, headers = self.vehicle_service.GetAllVehicles()
        
        if vehicles:
            print(tabulate(vehicles,headers=headers, tablefmt="psql"))
            with open("VehicleReport.csv","w",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(vehicles)
        else:
            print("No vehicles found")
