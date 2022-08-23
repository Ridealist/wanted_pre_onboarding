## wanted_pre_onboarding

### 1-1. Link
https://www.wanted.co.kr/events/pre_ob_be_4

### 1-2. Requirements Specification
https://bow-hair-db3.notion.site/4-82b986ae35454252a3a950f54e57af9b

#

## Project Overview

### Environment

- set Django version 3.2
- set Django-Rest-Framework version 3.12


### 3rd_Party_apps

- django-extensions
  - 확장 모델, 확장 command shell
- coverage
  - test coverage 측정
- factory-boy
  - test datasets 생성
- drf-spectacular
  - OpenAPI 3.0 문서 생산

# 

## 요구사항 분석

### 1. Announce (채용공고 등록 및 열람)

- models :
  - Announcement (채용공고)
  - Company (회사)
        
- serializer:
  - Company-- (회사 정보 json화)  
    -> nested serializer로 활용
  - AnnounceRegister-- (채용 공고 등록/수정/삭제)
  - AnnounceList-- (채용 공고 목록/검색)
  - AnnounceDetail-- (채용 공고 상세 페이지)
- views
  - AnnouncementViewSet
    - viewset action에 따라 별도 serializer class return
- filter_backends
  - SearchFilter (검색 기능 구현)

### 2. Apply (채용 지원)

- models: 
  - Apply
    - unique constraints 적용 (1회만 지원 가능)
- serializer
  - Apply--
    - unique together validator 적용 (1회만 지원 가능)
- views:
  - ApplyViewSet
    - Create 기능만 구현 (지원'만' 가능)

### 3. User (사용자)

- models: User
  - Abstract User model 상속
