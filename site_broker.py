from typing import List

from data_broker import DataBroker
from data_models import SiteStatus


class SiteBroker:
    def __init__(self):
        # Stores the latest status of each site -> Dict[int, SiteStatus]
        # Format: site_id -> SiteStatus
        self.site_status = {}

        # Initialize all sites as up
        for site_id in range(1, 11):
            self.site_status[site_id] = SiteStatus(
                status=True,
                last_failure_time=float('-inf'),
                site_log=[(0, True)]
            )

    def is_site_up(self, site_id: int) -> bool:
        return self.site_status[site_id].status

    def get_available_sites(self, data_id: str, data_broker: DataBroker) -> List[int]:
        possible_sites = data_broker.get_sites_for_data(data_id)
        return [site_id for site_id in possible_sites if self.is_site_up(site_id)]
