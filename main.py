import smartpy as sp


class Race:
    HORSES_MAX_AMOUNT = 50

    def __init__(self):
        self.init(
            horse_ids=sp.set(0),
            started_at=sp.timestamp(0),
            ended_at=sp.timestamp(0),
            # horse_count=sp.nat(0), # TODO: possibly not needed
        )

    def get_type():
        return sp.TRecord(
            horse_ids=sp.TSet,
            started_at=sp.TTimestamp,
            ended_at=sp.TTimestamp,
        )

    def add_horse(self, horse_id: sp.TNat):
        sp.verify(
            len(horse_ids) >= HORSES_MAX_AMOUNT,
            message="the amount of horses in a race may not exceed.{}".format(HORSES_MAX_AMOUNT)
        )
        self.horse_ids.append(horse_count)

    def delete_horse(self, horse_id: sp.TNat):
        sp.verify(len(horse_ids) > 0, message="nothing to delete: there're no horses")
        self.horse_ids.remove(horse_id)

    def is_active(self):
        return (started_at > sp.timestamp(0)) and (ended_at == sp.timestamp(0))


class RaceManager(sp.Contract):
    def __init__(self):
        self.init(
            races=sp.big_map(tkey=sp.TNat, tvalue=Race.get_type())
        )

    @sp.entry_point
    def add_race(self, new_race):
        self.update_initial_storage(races.append(new_race))

    @sp.entry_point
    def start_race(self, race_id):
        any_active_races = any(x.is_active() for x in races)
        sp.verify(~any_active_races, message="there's at least 1 active race going on now; wait for it to finish")

        #TODO will this update it in-place?
        for x in self.data.races:
            if x.id == race_id:
                x.started_at = sp.now


# to simulate smart contract events
class EventManager(sp.Contract):
    def __init__(self):
        pass

    @sp.entry_point
    def trigger_add_race(self, params):
        pass

    @sp.entry_point
    def trigger_start_race(self, params):
        pass