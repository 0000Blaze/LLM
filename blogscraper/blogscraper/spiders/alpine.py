import scrapy
from blogscraper.items import BlogscraperItem


class MagicalnepalSpider(scrapy.Spider):
    name = "magicalnepal"
    allowed_domains = ["magicalnepal.com"]
    urls = [
    "https://alpineclubofhimalaya.com/blog/",
    "https://alpineclubofhimalaya.com/staying-healthy-in-nepal/",
    "https://alpineclubofhimalaya.com/2019-novel-coronavirus-covid-19-travel-updates/",
    "https://alpineclubofhimalaya.com/terms-and-condition/",
    "https://alpineclubofhimalaya.com/travel-insurances/",
    "https://alpineclubofhimalaya.com/trip-special/",
    "https://alpineclubofhimalaya.com/travel-info/",
    "https://alpineclubofhimalaya.com/travel-insurances-2/",
    "https://alpineclubofhimalaya.com/meet-travel-experts/",
    "https://alpineclubofhimalaya.com/nepal-government-to-cancel-7-day-quarantine-for-tourists/",
    "https://alpineclubofhimalaya.com/covid-19-update-government-of-nepal/",
    "https://alpineclubofhimalaya.com/mount-everest-new-height-8848-86/",
    "https://alpineclubofhimalaya.com/nepal-is-now-open-to-travellers-vaccinated-with-covid-19-vaccines/",
    "https://alpineclubofhimalaya.com/best-season-to-travel-in-nepal/",
    "https://alpineclubofhimalaya.com/important-note/",
    "https://alpineclubofhimalaya.com/guide-for-trekking-in-nepal/",
    "https://alpineclubofhimalaya.com/visit-nepal/",
    "https://alpineclubofhimalaya.com/nepal/",
    "https://alpineclubofhimalaya.com/best-day-tour-in-nepal/",
    "https://alpineclubofhimalaya.com/how-to-trek-to-everest-base-camp/",
    "https://alpineclubofhimalaya.com/why-travel-with-alpine-club-of-himalaya/",
    "https://alpineclubofhimalaya.com/the-10-major-festivals-in-nepal/",
    "https://alpineclubofhimalaya.com/best-historical-places-to-visit-in-nepal/",
    "https://alpineclubofhimalaya.com/trek-in-nepal/",
    "https://alpineclubofhimalaya.com/explore-nepal-to-gain-beautiful-and-amazing-mountain-views/",
    "https://alpineclubofhimalaya.com/latest-travel-advisory-of-nepal/",
    "https://alpineclubofhimalaya.com/top-10-treks-in-nepal/",
    "https://alpineclubofhimalaya.com/11-interesting-facts-about-nepal-which-will-amuse-you/",
    "https://alpineclubofhimalaya.com/how-to-train-for-the-everest-base-camp-trek/",
    "https://alpineclubofhimalaya.com/trekking-guide-in-nepal/",
    "https://alpineclubofhimalaya.com/10-reasons-why-you-need-to-hire-a-local-guide-for-the-kanchenjunga-trek/",
    "https://alpineclubofhimalaya.com/city-tour-in-nepal/",
    "https://alpineclubofhimalaya.com/bhutan-welcomes-tourists-from-september-23-2022/",
    "https://alpineclubofhimalaya.com/short-treks-in-nepal/",
    "https://alpineclubofhimalaya.com/10-extreme-adventure-sports-in-nepal-you-should-dare/",
    "https://alpineclubofhimalaya.com/travelers-must-reach-the-international-airport-3-hours-before-their-scheduled-flight/",
    "https://alpineclubofhimalaya.com/great-reasons-to-do-the-annapurna-base-camp-trek/",
    "https://alpineclubofhimalaya.com/a-complete-guide-to-mardi-himal-trek/",
    "https://alpineclubofhimalaya.com/how-difficult-is-it-to-trek-annapurna-base-camp/",
    "https://alpineclubofhimalaya.com/major-tourist-attractions-in-nepal/",
    "https://alpineclubofhimalaya.com/10-sherpa-dishes-you-must-try-in-everest-base-camp-trek/",
    "https://alpineclubofhimalaya.com/best-treks-in-nepal-2022/",
    "https://alpineclubofhimalaya.com/how-will-trekking-expand-your-mind/",
    "https://alpineclubofhimalaya.com/top-5-best-heli-treks-in-nepal-in-2022/",
    "https://alpineclubofhimalaya.com/everest-base-camp-the-best-hike-i/",
    "https://alpineclubofhimalaya.com/tips-for-everest-base-camp-trek/",
    "https://alpineclubofhimalaya.com/everest-base-camp-trek-in-july-travel-tips-weather-and-more/",
    "https://alpineclubofhimalaya.com/drone-permit-in-nepal-a-thorough-guide/",
    "https://alpineclubofhimalaya.com/mera-peak-climbing-in-nepal/",
    "https://alpineclubofhimalaya.com/best-time-to-climb-mera-peak-in-nepal-weather-and-climate/",
    "https://alpineclubofhimalaya.com/mera-peak-vs-island-peak/",
    "https://alpineclubofhimalaya.com/everest-base-camp-in-november/",
    "https://alpineclubofhimalaya.com/mount-everest-base-camp/",
    "https://alpineclubofhimalaya.com/best-summer-treks-in-the-himalayas-of-nepal/",
    "https://alpineclubofhimalaya.com/reasons-to-visit-the-everest-region/",
    "https://alpineclubofhimalaya.com/trip-special-2/",
    "https://alpineclubofhimalaya.com/12-frequently-asked-questions-about-everest-base-camp-trek/",
    "https://alpineclubofhimalaya.com/exploring-nepal-foreign-tourists-prohibited-from-unguided-trekking/",
    "https://alpineclubofhimalaya.com/10-must-visit-attractions-in-tibet/",
    "https://alpineclubofhimalaya.com/everest-base-camp-trek-in-october/",
    "https://alpineclubofhimalaya.com/7-reasons-to-choose-a-trekking-agency-in-nepal/",
    "https://alpineclubofhimalaya.com/14-tips-for-a-successful-trek-to-the-everest-base-camp/",
    "https://alpineclubofhimalaya.com/annapurna-base-camp-trek/",
    "https://alpineclubofhimalaya.com/everest-base-camp-trek-full-guide/",
    "https://alpineclubofhimalaya.com/everest-trekking-in-nepal/",
    "https://alpineclubofhimalaya.com/new-chinese-embassy-rules/",
    "https://alpineclubofhimalaya.com/7-popular-hiking-routes-in-the-himalayas/",
    "https://alpineclubofhimalaya.com/reviving-tourism-in-nepal/",
    "https://alpineclubofhimalaya.com/important-notice-regarding-domestic-flight-from-kathmandu-to-lukla-and-return/",
    "https://alpineclubofhimalaya.com/accommodations-meals-weather-during-tibet-tour/",
    "https://alpineclubofhimalaya.com/alpine-club-of-himalaya-your-best-trekking-and-expeditions-in-nepal/",
    "https://alpineclubofhimalaya.com/everest-base-camp-trek-in-august/",
    "https://alpineclubofhimalaya.com/how-much-does-the-everest-base-camp-trek-cost/",
    "https://alpineclubofhimalaya.com/ama-dablam-trek-with-alpine-club-of-himalaya/",
    "https://alpineclubofhimalaya.com/exploring-the-mystical-gompas-of-lo-manthang-a-spiritual-journey-into-nepals-upper-mustang/",
    "https://alpineclubofhimalaya.com/discovering-5-fascinating-facts-on-langtang-valley-trek/",
    "https://alpineclubofhimalaya.com/exploring-the-majestic-annapurna-circuit/",
    "https://alpineclubofhimalaya.com/mardi-himal-trek-guide/",
    "https://alpineclubofhimalaya.com/shey-phoksundo-lake/",
    "https://alpineclubofhimalaya.com/exploring-the-enchanting-barun-valley-trek/",
    "https://alpineclubofhimalaya.com/explore-fantastic-and-breathtaking-mountain-views-in-trekking/",
    "https://alpineclubofhimalaya.com/alpine-club-of-himalaya-best-in-class-by-bookmundi/",
    "https://alpineclubofhimalaya.com/understand-the-highlights-of-trekking-in-nepal/",
    "https://alpineclubofhimalaya.com/explore-more-attractive-mountaineering-places-in-trekking/",
    "https://alpineclubofhimalaya.com/ama-dablam-expedition-see-beautiful-peak-valleys-of-nepal/",
    "https://alpineclubofhimalaya.com/testimonials/",
    "https://alpineclubofhimalaya.com/annapurna-base-camp-trek-is-favorite/",
    "https://alpineclubofhimalaya.com/sherpani-col-trek-25-days/",
    "https://alpineclubofhimalaya.com/charity-trek-in-nepal-a-soul-enriching-adventure-for-a-cause/",
    "https://alpineclubofhimalaya.com/phewa-lake-a-serene-oasis-in-nepals-pokhara-valley/",
    "https://alpineclubofhimalaya.com/beauty-of-gokyo-lake-and-gokyo-ri/",
    "https://alpineclubofhimalaya.com/the-wonders-of-chitwan-national-park-a-wildlife-paradise/",
    "https://alpineclubofhimalaya.com/everest-base-camp-trek-in-short/",
    "https://alpineclubofhimalaya.com/beauty-of-tengboche-monastery-trek/",
    "https://alpineclubofhimalaya.com/manaslu-trek-a-serene-himalayan-odyssey-for-adventure/",
    "https://alpineclubofhimalaya.com/discovering-the-hidden-gem-of-nepal-ruby-valley-trek/",
    "https://alpineclubofhimalaya.com/splendor-of-cho-la-pass-trek-a-himalayan-odyssey/",
    "https://alpineclubofhimalaya.com/mesmerizing-beauty-of-tilicho-lake-a-nature-lovers-paradise/",
    "https://alpineclubofhimalaya.com/discovering-the-peacefulness-of-the-mardi-himal-trek/",
    "https://alpineclubofhimalaya.com/a-comprehensive-guide-to-tsum-valley-trek/",
    "https://alpineclubofhimalaya.com/explore-the-enchanting-beauty-of-bhutan/",
    "https://alpineclubofhimalaya.com/unlocking-the-mystique-of-lhasa-a-comprehensive-guide/",
    "https://alpineclubofhimalaya.com/bumthang-cultural-trek-exploring-bhutans-rich-identity/"
]

    start_urls = [url for url in urls]

    def parse(self, response):
        item = BlogscraperItem()
        item["url"] = response.url,
        item["title"] = response.css(".entry-title::text").get()
        content_container = response.css(".entry-content")

        selected_tags = content_container.css("h1, h2,h3,h4,h5,h6, p, ul li")

        sections = []
        current_section = {"section_header": "", "section_content": []}
        for tag in selected_tags:
            if tag.root.tag in ["h2", "h3","h4"]:
                # Save the previous section if it has a header
                sections.append(current_section)
                current_section = {"section_header": "", "section_content": []}
                # current_section["section_header"] = tag.xpath("string()").get().strip()
                span_text = tag.css("span::text").get()
                current_section["section_header"] = (
                    span_text.strip() if span_text else tag.xpath("string()").get().strip()
                )

            else:
                # Append content to the current section
                text = tag.xpath("string()").get().strip()

                if text:
                    current_section["section_content"].append(text)

        # Append the last section if it has a header
        if current_section["section_content"]:
            sections.append(current_section)

        item["content"] = sections
        return item


