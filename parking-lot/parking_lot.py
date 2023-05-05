# Objects:
# parking lot, parking spot, entryGate, exitGate, vehical
# Behaviours:
# parking lot have parking spot
# vehical and parking lot have type
# entryGate give ticket
# exitGate takes payment

from abc import ABC, abstractmethod
from typing import List, Dict
from enum import Enum
from datetime import datetime


class ParkingSlot:
    def __init__(self, id, vehicalType) -> None:
        self.id = id
        self.vehicalType: VehicalType = vehicalType
        self.vehical: Vehical | None = None


class VehicalType(Enum):
    TWOWHEELER = 0
    FOURWHEELER = 1


class Vehical:
    def __init__(self, id: int, vehicalType: VehicalType) -> None:
        self.vehicalType = vehicalType
        self.id = id


class Ticket:
    def __init__(self, vehical: Vehical, slot: ParkingSlot) -> None:
        self.vehical = vehical
        self.startTime = datetime.now()
        self.slot = slot

    def close(self) -> None:
        self.endTime = datetime.now()


class Gate(ABC):
    @abstractmethod
    def exit(self, vehical: Vehical) -> None:
        pass

    @abstractmethod
    def entry(self, vehical: Vehical) -> None:
        pass


class EntryGate(Gate):
    def __init__(self, id, parkingLot) -> None:
        self.id = id
        self.parkingLot = parkingLot

    def entry(self, vehical: Vehical) -> None:
        print(f"Vehical {vehical.vehicalType} {vehical.id} entrying from EntryGate {self.id}")
        # check available parking slot
        if slot := self.parkingLot.getSlot(vehical):
            self.parkingLot.park(vehical, slot)
        else:
            print(f"No slot available for vehical {vehical.id} ({vehical.vehicalType})")

    def exit(self, vehical: Vehical) -> None:
        print(f"Vehical {vehical.id} cant exit from entry gate")


class ExitGate(Gate):
    def __init__(self, id, parkingLot) -> None:
        self.id = id
        self.parkingLot = parkingLot

    def entry(self, vehical: Vehical) -> None:
        print(f"Vehical {vehical.id} cant enter from exit gate")

    def exit(self, vehical: Vehical) -> None:
        if self.parkingLot.release(vehical):
            print(f"Vehical {vehical.vehicalType} {vehical.id} exiting from ExitGate {self.id}")


class ParkingLot:
    rate = {VehicalType.TWOWHEELER: 10, VehicalType.FOURWHEELER: 20}

    def __init__(self, numSlots: int, numEntryGate: int, numExitGate: int) -> None:
        self.entryGates: List[Gate] = [EntryGate(i, self) for i in range(numEntryGate)]
        self.exitGates: List[Gate] = [ExitGate(i, self) for i in range(numExitGate)]
        self.slots: List[ParkingSlot] = [
            ParkingSlot(i, VehicalType.TWOWHEELER if i % 2 else VehicalType.FOURWHEELER) for i in range(numSlots)
        ]
        self.vehicalTicket: Dict[Vehical, Ticket] = {}

    def getSlot(self, vehical: Vehical) -> ParkingSlot | None:
        availableSlots = list(
            filter(lambda slot: slot.vehicalType == vehical.vehicalType and not slot.vehical, self.slots)
        )
        if not availableSlots:
            return None
        return availableSlots[0]

    def park(self, vehical: Vehical, slot: ParkingSlot) -> None:
        # generate ticket
        ticket = Ticket(vehical, slot)
        # occupy parking slot
        slot.vehical = vehical
        self.vehicalTicket[vehical] = ticket

    def release(self, vehical: Vehical) -> bool:
        # check ticket
        if vehical not in self.vehicalTicket:
            return False
        # calculate fare
        ticket: Ticket = self.vehicalTicket[vehical]
        ticket.close()
        price = self.getPrice(ticket)
        print(f"Please pay {price}")
        # free up parking slot
        slot: ParkingSlot = ticket.slot
        slot.vehical = None
        return True

    def getPrice(self, ticket: Ticket) -> float:
        duration = (datetime.now() - ticket.endTime).total_seconds() / 60
        price = self.rate[ticket.vehical.vehicalType] * duration
        return price


parkingLot = ParkingLot(5, 1, 1)
car1 = Vehical(0, VehicalType.FOURWHEELER)
car2 = Vehical(1, VehicalType.FOURWHEELER)
car3 = Vehical(2, VehicalType.FOURWHEELER)
car4 = Vehical(3, VehicalType.TWOWHEELER)
parkingLot.entryGates[0].entry(car1)
parkingLot.entryGates[0].entry(car2)
parkingLot.entryGates[0].entry(car3)
parkingLot.entryGates[0].entry(car4)
parkingLot.exitGates[0].exit(car1)
parkingLot.exitGates[0].exit(car2)
parkingLot.exitGates[0].exit(car3)
parkingLot.exitGates[0].exit(car4)
