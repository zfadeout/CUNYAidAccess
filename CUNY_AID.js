document.addEventListener('DOMContentLoaded', () => {
    const collegeDropdown = document.getElementById('college-dropdown');
    const servicesDropdown = document.getElementById('services-dropdown');
    const confirmBtn = document.getElementById('confirm-btn');
    const outputArea = document.querySelector('.output-area');
  
    // Data mapping
    const messages = {
        'cuny-baruch': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'NYC Department of Homeless Services',
              address: '33 Beaver St, New York, NY 10004',
              phone: '212-361-6000',
              distance: '0.9 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Grand Central Neighborhood',
              address: '120 E 32nd St, New York, NY 10016',
              phone: '212-883-0680',
              distance: '0.55 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Main chance',
              address: '120 E. 32nd Street; New York, NY 10016',
              phone: '212-833-0680',
              distance: '0.57 Miles Away',
              recommended: 'No'
            },
            {
              name: '30th Street Mens Shelter Health Center',
              address: '400 E 30th St, New York, NY 10016',
              phone: '212-359-2820',
              distance: '0.77 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Bowery Residents Committee',
              address: '131 W 25th St, New York, NY 10001',
              phone: '212-803-5700',
              distance: '0.97 Miles Away',
              recommended: 'No'
            }
          ]
        },
        'cuny-staten': {
          'food': [
            {
              name: 'Staten Island Food Pantry',
              address: '120 Anderson Ave, Staten Island, NY 10303',
              phone: '718-273-2525',
              distance: '1.2 mi',
              recommended: 'Yes'
            },
            {
              name: 'St. Peter’s Soup Kitchen',
              address: '53 St. Marks Pl, Staten Island, NY 10301',
              phone: '718-447-3500',
              distance: '2.0 mi',
              recommended: 'No'
            },
            {
              name: 'Richmond Senior Center',
              address: '129 Stuyvesant Pl, Staten Island, NY 10301',
              phone: '718-720-2600',
              distance: '1.8 mi',
              recommended: 'Yes'
            },
            {
              name: 'Project Hospitality',
              address: '100 Park Ave, Staten Island, NY 10302',
              phone: '718-273-3400',
              distance: '2.1 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Community Health Center',
              address: '215 Bay St, Staten Island, NY 10301',
              phone: '718-448-4440',
              distance: '1.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Haven',
              address: '111 W 5th St, Staten Island, NY 10301',
              phone: '718-420-3030',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'Homeless Outreach Program',
              address: '432 Richmond Ave, Staten Island, NY 10312',
              phone: '718-356-1200',
              distance: '2.3 mi',
              recommended: 'Yes'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '5.0 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-craig': {
          'food': [
            {
              name: 'New York City Food Bank',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.3 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-206-0574',
              distance: '0.3 Miles Away',
              recommended: 'Yes'
            },
            {
              name: 'Breaking Ground',
              address: '505 Eighth Avenue, 5th FloorNew York, NY 10018',
              phone: '212-389-9300',
              distance: '0.45 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '0.66 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Olivieri',
              address: '257 West 30th Street; New York, NY 10001',
              phone: '212-213-6070',
              distance: '0.83 Miles Away',
              recommended: 'No'
            }
          ]
        },
        'cuny-health': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-law': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Borden Avenue Veterans Residence',
              address: '21-10 Borden Ave, Long Island City, NY 11101',
              phone: '718-784-5690',
              distance: '0.95 Miles Away',
              recommended: 'No'
            },
            {
              name: 'BRC',
              address: '146 Clay St, Brooklyn, NY 11222',
              phone: '212-613-0300',
              distance: '1.4 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Fairfield Inn (North Star)',
              address: '52-34 Van Dam St, Long Island City, NY 11101',
              phone: '212-226-6214',
              distance: '1.4 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Sweet Home',
              address: '3805 Hunters Point Ave, Long Island City, NY 11101',
              phone: '929-244-1520',
              distance: '1.8 Miles Away',
              recommended: 'No'
            }
          ]
        },
        'cuny-guttman': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-brooklyn': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Breaking Grounds Safe Haven',
              address: '781 Clarkson Ave, Brooklyn, NY 11203',
              phone: '718-360-8000',
              distance: '3.3 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Armory Mens Shelter',
              address: '1322 Bedford Ave, Brooklyn, NY 11216',
              phone: '718-636-3908',
              distance: '5.3 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Ready Willing and Able',
              address: '520 Gates Ave, Brooklyn, NY 11216',
              phone: '718-628-3223',
              distance: '6.2 Miles Away',
              recommended: 'No'
            },
            {
              name: 'CAMBA The Gathering Place',
              address: '2402 Atlantic Ave, Brooklyn, NY 11233',
              phone: '718-385-8726',
              distance: '1.8 Miles Away',
              recommended: 'No'
            }
          ]
        },
        'cuny-city': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-hunter': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Samaritan Village',
              address: '225 E 53rd St, New York, NY 10022',
              phone: '',
              distance: '1.2 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Lalitamba Saranam',
              address: 'PO Box 131 New York, NY 10024',
              phone: '212-873-0140',
              distance: '2.2 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-206-0574',
              distance: '2.7 Miles Away',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '2.8 Miles Away',
              recommended: 'No'
            }
          ]
        },
        'cuny-john-jay': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.1 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.4 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Ali Forney Center',
              address: '307 W 38th St, New York, NY 10018',
              phone: '212-290-0080',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Covenant House New York',
              address: '460 W 41st St, New York, NY 10036',
              phone: '212-613-0300',
              distance: '1.2 mi',
              recommended: 'No'
            },
            {
              name: 'New York City Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-queens': {
          'food': [
            {
              name: 'Queens Community House',
              address: '108-25 62nd Dr, Forest Hills, NY 11375',
              phone: '718-592-5757',
              distance: '2.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '5.5 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '6.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '6.2 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Safe Space',
              address: '89-74 162nd St, Queens, NY 11432',
              phone: '718-526-2400',
              distance: '4.0 Miles Away',
              recommended: 'Yes'
            },
            {
              name: 'Restfull Nights Organization',
              address: '106-38 150th St, South Jamaica, NY 11435',
              phone: '718-954-5744',
              distance: '4.9 Miles Away',
              recommended: 'No'
            },
            {
              name: 'The Landing Family Shelter',
              address: '94-00 Ditmars Blvd, East Elmhurst, NY 11369',
              phone: '718-226-0414',
              distance: '5.9 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Sweet Home',
              address: '3805 Hunters Point Ave, Long Island City, NY 11101',
              phone: '929-244-1520',
              distance: '9.1 Miles Away',
              recommended: 'No'
            }
          ]
        },
        'cuny-york': {
          'food': [
            {
              name: 'York College Food Pantry',
              address: '94-20 Guy R Brewer Blvd, Jamaica, NY 11451',
              phone: '718-262-2000',
              distance: '1.2 mi',
              recommended: 'Yes'
            },
            {
              name: 'Queens Community House',
              address: '108-25 62nd Dr, Forest Hills, NY 11375',
              phone: '718-592-5757',
              distance: '3.0 mi',
              recommended: 'No'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '5.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '5.8 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Homeless Outreach Program',
              address: '122-02 82nd Ave, Kew Gardens, NY 11415',
              phone: '718-830-0973',
              distance: '1.5 mi',
              recommended: 'Yes'
            },
            {
              name: 'NYC Rescue Mission',
              address: '90 Lafayette St, New York, NY 10013',
              phone: '212-226-6214',
              distance: '5.5 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '5.8 mi',
              recommended: 'Yes'
            },
            {
              name: 'Safe Horizon Streetwork Harlem',
              address: '209 W 125th St, New York, NY 10027',
              phone: '212-695-2220',
              distance: '6.0 mi',
              recommended: 'No'
            }
          ]
        },
        'cuny-medgar-evers': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.5 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '2.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Armory Mens Shelter',
              address: '1322 Bedford Ave, Brooklyn, NY 11216',
              phone: '718-636-3908',
              distance: '1.3 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Breaking Grounds Safe Haven',
              address: '781 Clarkson Ave, Brooklyn, NY 11203',
              phone: '718-360-8000',
              distance: '2.3 Miles Away',
              recommended: 'No'
            },
            {
              name: 'Ready Willing and Able',
              address: '520 Gates Ave, Brooklyn, NY 11216',
              phone: '718-628-3223',
              distance: '2.5 Miles Away',
              recommended: 'Yes'
            },
            {
              name: 'Providence House',
              address: '703 Lexington Ave, Brooklyn, NY 11221',
              phone: '718-455-0197',
              distance: '3.3 Miles Away',
              recommended: 'No'
            }
           ]
          },
        'cuny-King': {
          'food': [
            {
              name: 'Food Bank for New York City',
              address: '39 Broadway, New York, NY 10006',
              phone: '212-566-7855',
              distance: '1.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'City Harvest',
              address: '6 E 32nd St, New York, NY 10016',
              phone: '212-229-8227',
              distance: '1.5 mi',
              recommended: 'No'
            },
            {
              name: 'The Bowery Mission',
              address: '227 Bowery, New York, NY 10002',
              phone: '212-674-3456',
              distance: '2.0 mi',
              recommended: 'Yes'
            },
            {
              name: 'Holy Apostles Soup Kitchen',
              address: '296 9th Ave, New York, NY 10001',
              phone: '212-924-0173',
              distance: '1.8 mi',
              recommended: 'No'
            }
          ],
          'shelter': [
            {
              name: 'Breaking Grounds Safe Haven',
              address: '781 Clarkson Ave, Brooklyn, NY 11203',
              phone: '718-360-8000',
              distance: '8.7 Miles Away',
              recommended: 'No'
            }
          ]
        }
      };
  
    function updateOutput(college, service) {
      outputArea.innerHTML = '';
      if (messages[college] && messages[college][service]) {
        const list = document.createElement('ul');
        
        messages[college][service].forEach((entry) => {
          const listItem = document.createElement('li');
          
          const content = `
            <strong>${entry.name}</strong><br>
            <ul>
              <li><strong>Address:</strong> ${entry.address}</li>
              <li><strong>Phone:</strong> ${entry.phone}</li>
              <li><strong>Distance:</strong> ${entry.distance}</li>
              <li><strong>Recommended by CUNY:</strong> ${entry.recommended}</li>
            </ul>
          `;
          
          listItem.innerHTML = content;
          list.appendChild(listItem);
        });
  
        outputArea.appendChild(list);
      } else {
        outputArea.textContent = 'No information available for this selection.';
      }
    }
  
    confirmBtn.addEventListener('click', () => {
      const selectedCollege = collegeDropdown.value;
      const selectedService = servicesDropdown.value;
      updateOutput(selectedCollege, selectedService);
    });
  });
  
