def get_special_ability(html_source):
  return html_source.xpath('//table[@class="hero-abilities-table"]//tr[4]/td//text()')[1]

if __name__ == '__main__':
  import urllib.request as ur
  from lxml import html
  url = 'https://guardiantales.wiki/heroes/plitvice/'
  html_source = html.parse(ur.urlopen(url))
  print('Name: {}'.format(html_source.xpath('//h1/text()')[0][1:-1]))
  print('Special Ability: {}'.format(get_special_ability(html_source)))

