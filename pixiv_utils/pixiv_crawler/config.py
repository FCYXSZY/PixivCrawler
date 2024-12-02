import dataclasses
import datetime
import pprint
from typing import Dict, Tuple

from .utils import printInfo


@dataclasses.dataclass
class RankingConfig:
    # Start date
    start_date: datetime.date = datetime.date(2022, 8, 1)
    # Date range: [start, start + range - 1]
    range: int = 1
    # Which ranking list
    ranking_modes: Tuple = (
        "daily",
        "weekly",
        "monthly",
        "male",
        "female",
        "daily_ai",
        "daily_r18",
        "weekly_r18",
        "male_r18",
        "female_r18",
        "daily_r18_ai",
    )
    mode: str = "daily"  # Choose from the above
    # Illustration, manga, ugoira, all
    content_modes: Tuple = ("all", "illust", "manga", "ugoira")
    content_mode: str = "all"  # Choose from the above
    # Download top k in each ranking
    num_artwork: int = 50

    def __post_init__(self):
        assert self.mode in self.ranking_modes, f"Mode {self.mode} not supported"
        assert (
            self.content_mode in self.content_modes
        ), f"Content mode {self.content_mode} not supported"


@dataclasses.dataclass
class DebugConfig:
    # Whether to print verbose debug information
    verbose: bool = False
    # Whether to print error information
    show_error: bool = False


@dataclasses.dataclass
class NetworkConfig:
    # Proxy setting, you should customize your proxy setting accordingly. Default is for clash
    proxy: Dict = dataclasses.field(default_factory=lambda: {"https": "127.0.0.1:7890"})
    # Common request header
    headers: Dict = dataclasses.field(
        default_factory=lambda: {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        }
    )


@dataclasses.dataclass
class UserConfig:
    # Access your pixiv user profile to find this, e.g. https://www.pixiv.net/users/xxxx
    user_id: str = "49934750"
    # Your cookie, you can find it in the browser developer tool (README for more details)
    cookie: str = "first_visit_datetime_pc=2023-12-09%2021%3A31%3A13; p_ab_id=0; p_ab_id_2=6; p_ab_d_id=244589072; yuid_b=NlCVUYk; privacy_policy_notification=0; a_type=0; b_type=0; login_ever=yes; cc1=2024-12-02%2018%3A14%3A40; __cf_bm=RTHNU1H3qPlklvFwlIkCQSEB5nb08HwInuFn_N4s.70-1733130880-1.0.1.1-YY5r5u6va0NVdLKzsS1kU9T.0UfYYMvwNVKRYnUds5T0QLfRf8Y4cRWRKZwCIBo7W2xwyTwLaafQlIRbdvPV4mD0XR34eup_hy530v7ts8I; cf_clearance=jd8kguS4KtmtUhi8QBLE33yQq8GrZpiSl4VfmnmYozM-1733130883-1.2.1.1-4MH9fJ03.Sq296hSmRqQ4DkEvUb_ZEJRzQRHQY0f5JovlU14ukPsm0wSeXHUxEdYy9yzeYDKIiYABOpFpLqU8c.uX5PxBDPxoLLqMaVAreipvrV_gdG7.0GaVNNr6X4m_U_8SQquNgD2VhUopK4x6WdeOVDk6ziOyv93.bxexfBrv3xJCSrCA3ghpd_DTAoSHAV4WUnc8S86AtJPrLJBFzLFgrVYXuSpFQ._jhYjN0ujN__F57tfmlqsH51EIv.aJnDuRPMEAqpb7vc7v9i2jlO1DkFLKu2b7ldeomkSZJN4SSSLQ.gbftcRuAThMDCrPWwoE19hKRWZRbjox.Kj6L7MaaCTQ5xBFgSBLQLE16kDNMoxUhrcg5FlPs5twEbTyMIIdg2_GYSb2hriQZsyJQ; _gid=GA1.2.1495165893.1733130889; PHPSESSID=49934750_RhmHljfbL1ypkFkEK6WDe9G7fwsFbmZX; device_token=8356e6c1013cc6294b3a3f7956959538; privacy_policy_agreement=7; _ga_MZ1NL4PHH0=GS1.1.1733130893.7.0.1733130898.0.0.0; c_type=20; _im_vid=01JE3ADR0ZXFNSQ376V4P2MDPF; _ga_75BBYNYN9J=GS1.1.1733130886.10.1.1733131191.0.0.0; _ga=GA1.2.565933053.1702125080"


@dataclasses.dataclass
class DownloadConfig:
    timeout: float = 4  # Timeout for requests
    retry_times: int = 10  # Retry times for requests
    fail_delay: float = 1  # Waiting time (s) after failure
    store_path: str = "images"  # Image save path
    with_tag: bool = True  # Whether to download tags to a separate json file
    url_only: bool = False  # Only download artwork urls
    num_threads: int = 12  # Number of parallel threads
    thread_delay: float = 1  # Waiting time (s) after thread start


ranking_config = RankingConfig()
debug_config = DebugConfig()
network_config = NetworkConfig()
user_config = UserConfig()
download_config = DownloadConfig()


def displayAllConfig():
    infos = {
        "Ranking Config": dataclasses.asdict(ranking_config),
        "Debug Config": debug_config,
        "Network Config": network_config,
        "User Config": user_config,
        "Download Config": download_config,
    }
    for key, value in infos.items():
        printInfo(key + ":")
        pprint.pprint(value)
    print()
