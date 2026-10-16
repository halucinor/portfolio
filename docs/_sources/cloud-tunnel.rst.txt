사설 네트워크를 활용한 메트릭 수집 설정 자동화 시스템
=====================================================

**수행 기간 : 2024.07 ~ 2024.08 (2개월)**

    프로젝트 개요
    -------------

    .. image:: _static/cloud-tunnel/모니터링-개요.png
        :align: center
        :width: 800px

    **고객의 사설 네트워크를 통해 메트릭 수집 환경을 구성 과정을 자동화 시키는 시스템을 개발하는 프로젝트 입니다.**

    고객의 사설 네트워크는 외부 네트워크에 연결되어 있지 않기 때문에 메트릭 수집을 위한 모니터링 서버와 통신을 위해 추가 설정이 필요합니다.
    이를 위해 ``Podman 컨테이너`` 를 활용해 사설 네트워크와 모니터링 서버를 ``L2 통신`` 할 수 있는 환경을 **고객 네트워크 생성 시 자동으로 구성** 하는 시스템을 개발하였습니다.


핵심 기능
---------

    - 고객 사설 네트워크 생성 시 메트릭 수집 서버와 ``L2 통신`` 을 지원하는 ``Podman 컨테이너`` 생성
    - 사설 네트워크와 컨테이너를 연결하는 ``VLAN 설정``
    - 서브넷 생성 시 컨테이너와 연결하는 ``VIP(Port)`` 생성 및 라우팅 설정
    - 로드밸런서 생성 시 주기적으로 로드밸런서 데이터를 전송하는 스크립트 실행
    - 에러 발생 시 수동처리 및 마이그레이션 지원을 위해 자동화 과정을 API로 제공

    위 과정을 ``자동화`` 하여 메트릭 모니터링이 가능한 환경을 구성

    .. image:: _static/cloud-tunnel/터널-자동화-흐름.png
        :align: center
        :width: 800px

역할 및 기여
------------

    - 시스템 및 소프트웨어 아키텍처 설계
    - REST API 서버 구현
    - kafka 컨슈머 설계 및 구현
    - 프로젝트 매니저

개발 환경
---------

    - Language : ``Python 3.11``
    - Framework : ``FastAPI``
    - Library ``confluent_kafka``, ``Sqlalchemy``, ``Alembic``, ``Dependency injector``
    - Cloud Infra : ``Openstack``
    - DB : ``MySql``
    - MQ : ``Kafka``
    - Infra : ``Podman``
    - Monitoring System: ``Zabbix``

kafka 컨슈머 설계
-----------------

    .. image:: _static/cloud-tunnel/터널-아키택처.png
        :align: center
        :width: 800px

    - 이벤트 소스 : Openstack
    - 이벤트 소비자 : cloud-tunnel 서버

    1. 고객의 네트워크 생성 요청
    2. Openstack에서 네트워크 생성 완료 이벤트 발생
    3. cloud-tunnel에서 이벤트 수신
    4. Podman Container 생성 및 네트워크 연결 설정

kafka 메시지 Consumer
^^^^^^^^^^^^^^^^^^^^^

    .. image:: _static/cloud-tunnel/메시지-처리-흐름.png
        :align: center
        :width: 800px

    1. Openstack 이벤트를 메시지 객체로 변환
    2. 메시지를 처리할 수 있는 handler로 작업 분배

시퀀스 다이어그램
-----------------

1. 네트워크 생성시
^^^^^^^^^^^^^^^^^^

    .. image:: _static/cloud-tunnel/네트워크-생성.png
        :align: center
        :width: 800px

    1. 네트워크 생성완료 시 Openstack 이벤트 발생
    2. Podman 호스트 서버에 podman network 생성 요청
    3. Podman 컨테이너 생성 및 실행 요청

2. 서브넷 생성시
^^^^^^^^^^^^^^^^

    .. image:: _static/cloud-tunnel/서브넷-생성.png
        :align: center
        :width: 800px

    1. 서브넷 생성 시 Openstack 이벤트 발생
    2. 서브넷에 Podman 컨테이너와 통신할 수 있는 VIP(NIC) 생성
    3. Podman 컨테이너에 생성되어있는 스크립트를 실행하여 VIP와 연결

3. 로드밸런서 생성시
^^^^^^^^^^^^^^^^^^^^

    .. image:: _static/cloud-tunnel/로드밸런서-생성.png
        :align: center
        :width: 800px

    1. LB 생성 시 Openstack 이벤트 발생
    2. Podman 컨테이너에 생성되어있는 LB 연결 스크립트를 실행