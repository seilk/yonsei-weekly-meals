from src.parsers.aramark import day_key_from_label, parse_aramark_html
from src.parsers.yonsei import extract_week_data_json


def test_extract_week_data_json_basic() -> None:
    html = '<script>var weekData = [[{"campusName":"신촌","cls":"sc","refectory":[]}]];</script>'
    parsed = extract_week_data_json(html)
    assert isinstance(parsed, list)
    assert parsed[0][0]["campusName"] == "신촌"


def test_day_key_from_label() -> None:
    assert day_key_from_label("월(02/23)") == "mon"
    assert day_key_from_label("금(02/27)") == "fri"
    assert day_key_from_label("unknown") is None


def test_parse_aramark_html_section() -> None:
    html = """
    <div class="section1">
      <ul>
        <li class="list">
          <dl>
            <dt>한식 <span>월(02/23)</span></dt>
            <dd>메뉴A<br/>메뉴B<br/></dd>
          </dl>
        </li>
      </ul>
    </div>
    """
    parsed = parse_aramark_html(html, meal_time="m")
    assert parsed["mon"][0]["meal_time"] == "조식"
    assert parsed["mon"][0]["category"] == "한식"
    assert parsed["mon"][0]["items"] == ["메뉴A", "메뉴B"]
