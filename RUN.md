# 안드로이드 매핑 앱 실행

1. `python setup_android.py`
2. 생성된 AndroidProject를 Android Studio에서 엽니다.
3. JDK 17, Android SDK 35, AGP 8.9.2와 Gradle 8.11.1을 사용합니다. Gradle wrapper 바이너리는 포함하지 않았습니다. 로컬 Gradle을 설정하거나 Gradle 8.11.1에서 `gradle wrapper --gradle-version 8.11.1`로 생성하세요.
4. 에뮬레이터 또는 실제 휴대폰에서 Run. 에뮬레이터는 Extended Controls > Displays로 보조 디스플레이를 시험할 수 있습니다.

네 모서리 드래그, 볼록 사각형 검사, 이미지 불러오기, 투사 영역 밖 마스킹, 사진 원근 변환, 좌표 저장·불러오기를 구현했습니다. 출력은 Android Presentation으로 편집 핸들을 제외한 화면만 보냅니다.

일반 HDMI 영상 출력은 휴대폰 하드웨어 지원이 필요합니다. 단순 화면 미러링을 앱이 임의로 독립 화면으로 바꿀 수는 없습니다.

이 첫 버전은 이미지 1장·영역 1개입니다. 동영상, 여러 영역, 자유형 마스크, 무선 연결은 아직 없습니다.
Android SDK/JDK가 이 개발 환경에 없어 APK 빌드와 실제 프로젝터 검증은 하지 못했습니다.
