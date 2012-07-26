from django.conf import settings

PARSER = getattr(settings, "PORTFOLIO_PARSER", ["portfolio.markdown_parser.parse", {}])