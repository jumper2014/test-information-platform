# coding=utf-8
# common constant

# jenkins master server url，port
jenkins_server_url = 'http://10.4.0.1:8080/'

# User Id API Token
user_id = 'jenkins_user'
api_token = 'a36ea26fdd50a32f652e8d56d7cb86e3'  # need to be updated


# job_name
job_names = [
    ##########################
    # sdk test
    ##########################
    'p2pclient_ut',
    'BJ-Auto-Test-Linux_SDK_Start',
    'BJ-Auto-Test-Linux_SDK_Check',
    'BJ-Auto-Test_Linux_SDK_Api',
    'BJ-Auto-Test_Linux_SDK_Init',
    'BJ-Auto-Test_Linux_SDK_Login',
    'BJ-Auto-Test_Linux_SDK_Penetrate',
    'BJ-Auto-Test_Linux_SDK_Routine',

    ##########################
    # server test
    ##########################
    'p2pserver_ut',
    'BJ-Auto-Test_Platform_Collect_Log',
    'BJ-Auto-Test_Server_API_Channel',
    # 'BJ-Auto-Test_Server_API_Dir',
    # 'BJ-Auto-Test_Server_API_Panel',
    'BJ-Auto-Test_Server_API_Report',
    'BJ-Auto-Test_Server_API_Stats',
    'BJ-Auto-Test_Server_API_Stun-hub',
    'BJ-Auto-Test_Server_API_Stun_Rrpc',
    'BJ-Auto-Test_Server_API_Stun_Stun',
    'BJ-Auto-Test_Server_API_Stun_Thunder',
    'BJ-Auto-Test_Server_API_TS',
    'BJ-Auto-Test_Server_API_p2p-ops',
    'BJ-Auto-Test_Server_API_Httpdns',
    'BJ-Auto-Test_Platform_Flume',
    'BJ-Auto-Test_Platform_Boss_Internal_Api',

    ##########################
    # deplopy build
    ##########################
    # 'BJ-Auto-Test-Deploy_Dir',
    'BJ-Auto-Test-Deploy_Funnel',
    'BJ-Auto-Test-Deploy_Get_DailyTest_Info',
    'BJ-Auto-Test-Deploy_httpdns',
    'BJ-Auto-Test-Deploy_kafka_flume',
    'BJ-Auto-Test-Deploy_p2p_channel',
    'BJ-Auto-Test-Deploy_p2p_live_channel',
    'BJ-Auto-Test-Deploy_p2p_stun2_go',
    'BJ-Auto-Test-Deploy_p2p_stun2_go_xunlei',
    'BJ-Auto-Test-Deploy_SRV_p2p_ops',
    'BJ-Auto-Test-Deploy_Stun-hub',
    'BJ-Auto-Test-Deploy_Tracker',
    'BJ-Auto-Test_DEPLOY_SRV_p2p_tracker_go',
    'BJ-Auto-Test_Zeus_Deploy',
    'develop_client_debug_build_windows',
    'develop_client_release_log_http_ubuntu64',
    'develop_client_release_nolog_http_centos',
    'develop_client_release_nolog_https_apk_sdk_ubuntu64'
]

# get last x bulid_times result
LAST_BUILD_TIMES = 8

# zentao bug date_size
RECENT_DATE_SIZE = 20

# feature_test page
EVERY_PAGE_SIZE = 20
